from watch.models import Anime

class AnimeHelper:
    @staticmethod
    def get_all():
        anime = Anime.objects.all()
        return anime
    
