from celery import shared_task
from service.pallets.voting import VotingQueries
from voting.models import Ranks


@shared_task
def get_node_ranks():

    voting_queries = VotingQueries()
    number = voting_queries.get_number_of_candidates()
    address_list = voting_queries.get_session_node_list(number)

    for address in address_list:
        accumulative_votes = voting_queries.get_node_accumulative_votes(address)
        node_metadata = voting_queries.get_node_metadata(address)
        data = {
            "node_id": "Dn" + address,
            "node_name": node_metadata['name'],
            "sharing_percent": node_metadata['sharing_percent'],
            "accumulative_votes": accumulative_votes,
        }
        ranks, created = Ranks.objects.update_or_create(
            node_id=data['node_id'],
            defaults=data
        )
        print({"node_id": ranks.node_id, "node_name": ranks.node_name, "sharing_percent": ranks.sharing_percent, "accumulative_votes": ranks.accumulative_votes,"created": created})

