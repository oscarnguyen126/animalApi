from django.shortcuts import get_object_or_404
from .serializers import AccountSerializer, AccountInfoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Account, Dog, Cat
from apps.cats.serializers import CatSerializer, ShowCatSerializer
from apps.dogs.serializers import DogSerializer, ShowDogSerializer
from rest_framework.decorators import api_view
from rest_framework import status


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()

    def list(self, request):
        serializer = AccountInfoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.create()
        account.save()
        return Response({"Result": serializer.data})

    def retrieve(self, request, pk=None):
        account = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountInfoSerializer(account)
        return Response(serializer.data)

    def update(self, request, pk=None):
        account = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account.username = request.data["username"]
        account.email = request.data["email"]
        account.password = request.data["password"]
        account.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        account = get_object_or_404(self.queryset, pk=pk)
        account.delete()
        return Response({"msg": "The account has been removed"})


# class PetViewSets(viewsets.ViewSet):
#     queryset = Account.objects.all()

#     def retrieve(self, request, account_pk, pk):
#         account = get_object_or_404(self.queryset, pk=account_pk)
#         serializer = AccountSerializer(account)
#         # select from cats
#         # where id = 2 and user_id = 1
#         dog = Dog.objects.filter(account_id=account_pk, id=pk
#         ).first()
#         cat = Cat.objects.filter(account_id=account_pk, id=pk).first()
#         # select from dogs
#         # where id = 2 and user_id = 1
        
#         return Response(serializer.data)


@api_view(['GET', 'PUT'])
def get_all_pets(request, id):
    account = Account.objects.all().filter(id = id).first()
    account_serializer = AccountInfoSerializer(account)
    dogs = Dog.objects.all().filter(account_id=id)
    cats = Cat.objects.all().filter(account_id=id)
    dog_serializer = DogSerializer(dogs, many=True)
    cat_serializer = CatSerializer(cats, many=True)

    pets = [dog_serializer.data, cat_serializer.data]
    content = {
        'user': account_serializer.data,
        'pets': pets
    }

    if request.method == 'PUT':
        payload = request.data

        account = Account.objects.filter(id = id).first()
        if not account:
            return Response(status=400, content="Account is not exist.")

        dog_ids = [pet['id'] for pet in payload['pets'] if pet['type'] == 'dog']
        cat_ids = [pet['id'] for pet in payload['pets'] if pet['type'] == 'cat']
        
        dogs = Dog.objects.filter(id__in=dog_ids)

        if len(dogs) != len(dog_ids):
            return Response(
                data=f"Dogs with ids={str(set(dog_ids) - set( [d.id for d in dogs]))} are not exist.",
                status=400
            )

        cats = Cat.objects.filter(id__in=cat_ids)
        if len(cats) != len(cat_ids):
            return Response(
                data=f"Cats with ids={str(set(cat_ids) - set( [d.id for d in cats]))} are not exist.",
                status=400
            )

        account.dogs.add(*dogs)
        account.cats.add(*cats)

        account.save()

        # TODO: add serializer then return response:
        # { "user": {....}, "pets": [{..type}]}
        dog_serializer = ShowDogSerializer(Dog.objects.all().filter(account_id=id), many=True)
        cat_serializer = ShowCatSerializer(Cat.objects.all().filter(account_id=id), many=True)
        pets = [dog_serializer.data, cat_serializer.data]
        content = {
            'users': AccountInfoSerializer(account).data,
            'pets': pets
        }

        return Response(content)

    return Response(content)
