class India:
    def capital(self):
        print("Capital: New Delhi")

    def language(self):
        print("Language: Hindi and many other regional languages")

    def country_type(self):
        print("Type: Republic")


class Japan:
    def capital(self):
        print("Capital: Tokyo")

    def language(self):
        print("Language: Japanese")

    def country_type(self):
        print("Type: Constitutional monarchy")


for country in [India(), Japan()]:
    country.capital()
    country.language()
    country.country_type()
    print()
