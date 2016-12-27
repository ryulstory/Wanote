from django.shortcuts import render
from django.http import HttpResponse
from wanote.photo.models import photo
# Create your views here.

#한개의 사진만 보기
def single_photo(request, photo_id):
	photo = photo.object.get(pk=photo_id)
	response_text = '<p>{photo_id}번...{photo_id}번 사진을 보여 드릴게요.</p>'
	response_text += '<p>{photo_url}</p>'

	return HttpResponse(response_text.format(
		photo_id=photo_id,
		photo_url=photo.image_file.url)
	)

#목록보기
def index(request, page=1, n):
	#한페이지당 사진 갯수
	per_page=n
	start_pos=(page-1)*per_page
	end_pos=start_pos+per_page
	#시간 역순으로 정리
	photo = photo.object.all().order_by('-created')[start_pos:end_pos]

