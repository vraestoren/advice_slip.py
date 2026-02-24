from requests import Session

class AdviceSlip:
	def __init__(self) -> None:
		self.api = "https://api.adviceslip.com"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_advice(self) -> dict:
		return self.session.get(f"{self.api}/advice").json()

	def get_advice_by_id(self, slip_id: int) -> dict:
		return self.session.get(f"{self.api}/advice/{slip_id}").json()

	def search_advice(self, query: str) -> dict:
		return self.session.get(
			f"{self.api}/advice/search/{query}").json()
