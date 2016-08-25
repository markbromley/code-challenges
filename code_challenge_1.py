import mechanize
from bs4 import BeautifulSoup

class EuclideanAlgorithm(object):
    """
    Standard implementation of Euclidean algorithm.
    """
    @staticmethod
    def solve(a, b):
        a, b = (b, a) if a < b else (a, b)
        return b if (a % b) == 0 else EuclideanAlgorithm.solve(b, a % b)

class QuantBet(object):
    """
    Handles the quantbet web page.
    """
    def __init__(self, url):
        self.url = url
        self.br = mechanize.Browser()

    def get_input_values(self):
        self.br.set_handle_robots(False) # ignore robots
        page = self.br.open(self.url)

        # Get input and calculate result
        soup = BeautifulSoup(page,"html5lib")
        strong_els = soup.find_all("strong")
        return int(strong_els[0].string), int(strong_els[1].string)

    def submit_answer(self, answer):
        # Submit result
        for form in self.br.forms():
            if form.attrs["id"] == "quiz":
                self.br.form = form
                break
        self.br.form["divisor"] = str(answer)
        res = self.br.submit()
        content = res.read()
        return content


if __name__ == "__main__":
    # Open page
    url = "http://quantbet.com/quiz"
    quantBet = QuantBet(url)
    a,b = quantBet.get_input_values()
    answer = EuclideanAlgorithm.solve(a,b)
    result = quantBet.submit_answer(answer)

    # Write out the results to a file
    with open("results.html", "w") as f:
        f.write(result)

    