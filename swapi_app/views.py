import random
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .services import SWAPIService
from .serializers import PersonSerializer


def get_related_entities(data, entity_type):
    related = []
    if entity_type == 'people' and 'homeworld' in data:
        related_data = SWAPIService.fetch_data_by_url(data['homeworld'])
        for resident_url in related_data.get('residents', []):
            if resident_url != data['url']:  # Not relating the character to himself
                resident_data = SWAPIService.fetch_data_by_url(resident_url)
                related.append({
                    "id": resident_url.split('/')[-2],
                    "name": resident_data['name'],
                    "relation": related_data['url']
                })
    return related


def get_random_related_entities(related_entities):
    random.shuffle(related_entities)
    return related_entities[:3]


@api_view(['GET'])
def get_character(request, id):
    try:
        data = SWAPIService.fetch_data_by_id('people', id)
    except Exception:
        return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)
    
    related_entities = get_related_entities(data, 'people') # related entities based on homeworld
    
    random_entities = get_random_related_entities(related_entities) # shuffle related entities
    data['related'] = random_entities
    
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
