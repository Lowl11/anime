from main.models import NavigationLink

class NavigationLinksHelper:
    @staticmethod
    def get_links():
        links = NavigationLink.objects.all()
        return links
