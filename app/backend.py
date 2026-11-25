import os

import requests

API_URL = os.environ.get("API_URL")  # set in Docker; unset on Streamlit Cloud


class RateLimited(Exception):
    pass


class Unavailable(Exception):
    pass


def warm_up():
    if not API_URL:  # direct mode: load model and index in this process
        from src.retrieve import _load
        _load()


def get_answer(question: str) -> dict:
    if API_URL:
        try:
            r = requests.post(f"{API_URL}/ask", json={"question": question}, timeout=120)
        except requests.ConnectionError:
            raise Unavailable
        if r.status_code == 429:
            raise RateLimited
        r.raise_for_status()
        return r.json()

    from groq import APIConnectionError, RateLimitError
    from src.generate import answer
    try:
        return answer(question)
    except RateLimitError:
        raise RateLimited
    except APIConnectionError:
        raise Unavailable