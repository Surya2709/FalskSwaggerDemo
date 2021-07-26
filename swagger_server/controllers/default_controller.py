import connexion
import six

from swagger_server.models.alert import Alert  # noqa: E501
from swagger_server.models.alert_array import AlertArray  # noqa: E501
from swagger_server.models.updatealert import Updatealert  # noqa: E501
from swagger_server import util


def alert_delete(alert_id):  # noqa: E501
    """delete alert

    takes the alert id as feed to remove the alert from the alert list # noqa: E501

    :param alert_id: id of the alert need to be removed
    :type alert_id: str

    :rtype: None
    """
    return 'do some magic!'


def alert_get(alert_id=None):  # noqa: E501
    """obtain alert  list

    get method to obtain all the alerts # noqa: E501

    :param alert_id: identifier for the alert
    :type alert_id: str

    :rtype: AlertArray
    """
    return 'do some magic!'


def alert_post(body):  # noqa: E501
    """add alerts

    Adds the alerts into the list  # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Alert.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def alert_put(body):  # noqa: E501
    """update the  alerts

    updates the alerts in the alerts list # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Updatealert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
