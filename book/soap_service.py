from spyne.service import ServiceBase
from spyne.application import Application
from spyne.decorator import rpc, srpc
from spyne.model import Integer, String, Unicode
from spyne.protocol.soap import Soap11
from .models import CategoryModel, PublisherModel, AuthoreModel, BookModel


class CategorySoap(ServiceBase):

    @srpc(_returns=Unicode)
    def list_category():
        objs = CategoryModel.objects.all()
        return (f"category_id:{obj.id}, authore_name:{obj.name}" for obj in objs)


class PublisherSoap(ServiceBase):

    @srpc(_returns=Unicode)
    def list_publisher():
        objs = PublisherModel.objects.all()
        return (f"publisher_id:{obj.id}, publisher_name:{obj.name}" for obj in objs)


class AuthoreSoap(ServiceBase):

    @srpc(_returns=Unicode)
    def list_authore():
        objs = AuthoreModel.objects.all()
        return (f"authore_id:{obj.id}, authore_name:{obj.name}" for obj in objs)
    

class BookSoap(ServiceBase):

    @srpc(_returns=Unicode)
    def list_book():
        objs = BookModel.objects.all()
        return (f"book_id:{obj.id}, book_name:{obj.name}, book_image:{obj.thumbnail}" for obj in objs)
    
    @srpc(Integer, _returns=Unicode)
    def detail_book(id):
        obj = BookModel.objects.get(pk=id)
        return (
            f"""book_id:{obj.id}, book_name:{obj.name},
              book_title:{obj.title}, book_description:{obj.description},
              book_date:{obj.date}, book_pages:{obj.pages}, book_thumbnail:{obj.thumbnail},
              book_category_id:{obj.category.id}, book_category_name:{obj.category.name},
              book_authore_id:{obj.authore.id}, book_authore_name:{obj.authore.name},
              book_publisher_id:{obj.publisher.id}, book_publisher_name:{obj.publisher.name}
            """
        )

application = Application(
        [CategorySoap, PublisherSoap, AuthoreSoap, BookSoap], 
        tns='django.soap.example',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )