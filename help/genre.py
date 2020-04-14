from watch.models import Genre

class GenreHelper:
    @staticmethod
    def get_genres():
        genre_list = Genre.objects.all()
        return genre_list
    
