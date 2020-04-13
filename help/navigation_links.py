from main.models import NavigationLink

class NavigationLinksHelper:
    @staticmethod
    def get_links():
        print('NavigationLinksHelper')
        print('get_links()')
        links = NavigationLink.objects.all()
        print('links: ')
        print(links)
        return links
