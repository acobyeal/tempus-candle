from django.views.generic import ListView, DetailView
from photo.models import Album, Photo
# blog.models.Post 클래스 임포트
from blog.models import Post

# 뷰 정의에서 템플릿 파일명을 지정하는 것이 일반적이지만,
# 여기서는 생략했으므로, 디폴트 템플릿명이 적욛됨.
# 디폴트 템플릿명은 모델명과 상속받는 제넥릭 뷰에 따라서 결정되는데,
# AlbumLV, AlbumDV, PhotoDV 뷰에 대한 디폴트 템플릿명은
# album_list.html, album_detail.html, photo_detail.html

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo

# ListView를 상속받아서 PostLV 작성
class PostLV(ListView) :
    model = Post
    # 기본값 'photo/photo_detail.html' 대신 지정 (3.1.4 URL 설계 항 참고)
    template_name = 'photo_detail.html'
    # 컨텍스트 객체 이름을 기본값(object_list)와 다르게 지정했지만,
    # 기본값(object_list)도 여전히 사용 가능함
    context_object_name = 'posts'
    # paginate_by = 5  # 페이지 당 5 개 객체를 처리하도록 지정
