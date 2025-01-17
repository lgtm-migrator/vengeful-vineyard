# flake8: noqa

from typing import Any

import pytest
from tests.fixtures import client, mock
from tests.response_time import check_response_time

ME_RESPONSE = [
    {
        "group_id": 1,
        "ow_group_id": 4,
        "name": "Drifts- og Utviklingskomiteen",
        "name_short": "Dotkom",
        "rules": "No rules",
        "image": "https://onlineweb4-prod.s3.eu-north-1.amazonaws.com/media/images/responsive/sm/0990ab67-0f5b-4c4d-95f1-50a5293335a5.png",
    }
]

ME_UPDATED_RESPONSE = [
    {
        "group_id": 1,
        "ow_group_id": 4,
        "name": "Drifts- og Utviklingskomiteen",
        "name_short": "DotkomUpdated",
        "rules": "No rules",
        "image": "https://onlineweb4-prod.s3.eu-north-1.amazonaws.com/media/images/responsive/sm/0990ab67-0f5b-4c4d-95f1-50a5293335a5.png",
    }
]

ME_NEW_USER_RESPONSE: list[dict[str, Any]] = []

ME_GROUPS_RESPONSE = [
    {
        "name": "Drifts- og Utviklingskomiteen",
        "name_short": "Dotkom",
        "rules": "No rules",
        "ow_group_id": 4,
        "image": "https://onlineweb4-prod.s3.eu-north-1.amazonaws.com/media/images/responsive/sm/0990ab67-0f5b-4c4d-95f1-50a5293335a5.png",
        "group_id": 1,
        "punishment_types": [
            {
                "name": "\u00d8lstraff",
                "value": 33,
                "logo_url": "./assets/beerOutlined.svg",
                "punishment_type_id": 1,
            },
            {
                "name": "Vinstraff",
                "value": 100,
                "logo_url": "./assets/wineOutlined.svg",
                "punishment_type_id": 2,
            },
            {
                "name": "Spritstraff",
                "value": 300,
                "logo_url": "./assets/spiritOutlined.svg",
                "punishment_type_id": 3,
            },
        ],
        "members": [
            {
                "ow_user_id": 2581,
                "first_name": "Brage",
                "last_name": "",
                "ow_group_user_id": 2224,
                "email": "email1@email.com",
                "user_id": 1,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1381,
                "first_name": "Amund",
                "last_name": "",
                "ow_group_user_id": 656,
                "email": "email2@email.com",
                "user_id": 2,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1383,
                "first_name": "Anh-Kha Nguyen",
                "last_name": "",
                "ow_group_user_id": 658,
                "email": "email3@email.com",
                "user_id": 3,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 2027,
                "first_name": "Anna Irene",
                "last_name": "",
                "ow_group_user_id": 1552,
                "email": "email4@email.com",
                "user_id": 4,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 2219,
                "first_name": "Billy Steen",
                "last_name": "",
                "ow_group_user_id": 2227,
                "email": "email5@email.com",
                "user_id": 5,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1705,
                "first_name": "B\u00f8rge",
                "last_name": "",
                "ow_group_user_id": 1052,
                "email": "email6@email.com",
                "user_id": 6,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1395,
                "first_name": "Carl",
                "last_name": "",
                "ow_group_user_id": 1551,
                "email": "email7@email.com",
                "user_id": 7,
                "active": True,
                "punishments": [],
            },
        ],
    }
]

ME_GROUPS_UPDATED_RESPONSE = [
    {
        "name": "Drifts- og Utviklingskomiteen",
        "name_short": "DotkomUpdated",
        "rules": "No rules",
        "ow_group_id": 4,
        "image": "https://onlineweb4-prod.s3.eu-north-1.amazonaws.com/media/images/responsive/sm/0990ab67-0f5b-4c4d-95f1-50a5293335a5.png",
        "group_id": 1,
        "punishment_types": [
            {
                "name": "\u00d8lstraff",
                "value": 33,
                "logo_url": "./assets/beerOutlined.svg",
                "punishment_type_id": 1,
            },
            {
                "name": "Vinstraff",
                "value": 100,
                "logo_url": "./assets/wineOutlined.svg",
                "punishment_type_id": 2,
            },
            {
                "name": "Spritstraff",
                "value": 300,
                "logo_url": "./assets/spiritOutlined.svg",
                "punishment_type_id": 3,
            },
        ],
        "members": [
            {
                "ow_user_id": 2581,
                "first_name": "BrageUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 2224,
                "email": "email1@email.com",
                "user_id": 1,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1381,
                "first_name": "AmundUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 656,
                "email": "email2@email.com",
                "user_id": 2,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 1383,
                "first_name": "Anh-Kha NguyenUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 658,
                "email": "email3@email.com",
                "user_id": 3,
                "active": True,
                "punishments": [],
            },
            {
                "ow_user_id": 2027,
                "first_name": "Anna IreneUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 1552,
                "email": "email4@email.com",
                "user_id": 4,
                "active": False,
                "punishments": [],
            },
            {
                "ow_user_id": 2219,
                "first_name": "Billy SteenUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 2227,
                "email": "email5@email.com",
                "user_id": 5,
                "active": True,
                "punishments": [],
            },
            # Removed user here
            {
                "ow_user_id": 1395,
                "first_name": "CarlUpdated",
                "last_name": "Updated",
                "ow_group_user_id": 1551,
                "email": "email7@email.com",
                "user_id": 7,
                "active": True,
                "punishments": [],
            },
            {  # Added user here
                "ow_user_id": 1998,
                "first_name": "FelixOriginal",
                "last_name": "Original",
                "ow_group_user_id": 1399,
                "email": "email8@email.com",
                "user_id": 8,
                "active": True,
                "punishments": [],
            },
        ],
    }
]


DEFAULT_PUNISHMENT_TYPES = [
    {
        "name": "Ølstraff",
        "value": 33,
        "logo_url": "./assets/beerOutlined.svg",
        "punishment_type_id": 1,
    },
    {
        "name": "Vinstraff",
        "value": 100,
        "logo_url": "./assets/wineOutlined.svg",
        "punishment_type_id": 2,
    },
    {
        "name": "Spritstraff",
        "value": 300,
        "logo_url": "./assets/spiritOutlined.svg",
        "punishment_type_id": 3,
    },
]

NEW_PUNISHMENT_TYPE_PAYLOAD = {
    "name": "Waffles",
    "value": 125,
    "logo_url": "./assets/beerOutlined.svg",
}

WAFFLES_PUNISHMENT_TYPE_RESPONSE = {
    "name": "Waffles",
    "value": 125,
    "logo_url": "./assets/beerOutlined.svg",
    "punishment_type_id": 4,
}


SELF_USER_ID = 1
OTHER_USER_ID = 4
OTHER_USER_NOT_IN_GROUP_ID = 10
SELF_USER_ACCESS_TOKEN = str(SELF_USER_ID)
OTHER_USER_ACCESS_TOKEN = str(OTHER_USER_ID)
OTHER_USER_NOT_IN_GROUP_ACCESS_TOKEN = str(OTHER_USER_NOT_IN_GROUP_ID)
SELF_USER_AUTHORIZATION = f"Bearer {SELF_USER_ACCESS_TOKEN}"
OTHER_USER_AUTHORIZATION = f"Bearer {OTHER_USER_ACCESS_TOKEN}"
OTHER_USER_NOT_IN_GROUP_AUTHORIZATION = f"Bearer {OTHER_USER_NOT_IN_GROUP_ACCESS_TOKEN}"


class TestOW:
    @pytest.mark.asyncio
    async def test_get_my_groups_missing_authorization(self, client: Any) -> None:
        response = await client.get("/group/me")
        assert response.status_code == 401 and response.json() == {
            "detail": "Missing authorization"
        }
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_unauthenticated(self, client: Any, mock: Any) -> None:
        response = await client.get(
            "/group/me", headers={"Authorization": "Bearer InvalidAuth"}
        )
        assert response.status_code == 401 and response.json() == {
            "detail": "Invalid access token"
        }

    @pytest.mark.asyncio
    async def test_get_my_groups(
        self,
        client: Any,
        mock: Any,
    ) -> None:
        response = await client.get(
            "/group/me", headers={"Authorization": SELF_USER_AUTHORIZATION}
        )

        assert response.status_code == 200
        assert response.json() == ME_RESPONSE

        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_other_user_in_group(
        self,
        client: Any,
        mock: Any,
    ) -> None:
        response = await client.get(
            "/group/me", headers={"Authorization": OTHER_USER_AUTHORIZATION}
        )

        assert response.status_code == 200
        assert response.json() == ME_RESPONSE

        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_members(self, client: Any) -> None:
        for c, group in enumerate(ME_RESPONSE):
            response = await client.get(f"/group/{group['group_id']}")

            assert response.status_code == 200
            assert response.json() == ME_GROUPS_RESPONSE[c]

            check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_update(self, client: Any) -> None:
        response = await client.get(
            "/group/me", headers={"Authorization": SELF_USER_AUTHORIZATION}
        )

        assert response.status_code == 200
        assert response.json() == ME_UPDATED_RESPONSE

        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_members_update(self, client: Any) -> None:
        for c, group in enumerate(ME_UPDATED_RESPONSE):
            response = await client.get(f"/group/{group['group_id']}")

            assert response.status_code == 200

            response_data = response.json()
            response_data["members"] = sorted(
                response_data["members"], key=lambda x: x["ow_user_id"]  # type: ignore
            )
            set_response = ME_GROUPS_UPDATED_RESPONSE
            set_response[c]["members"] = sorted(
                set_response[c]["members"], key=lambda x: x["ow_user_id"]  # type: ignore
            )
            assert response_data == set_response[c]

            check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_my_groups_other_not_in_group(
        self,
        client: Any,
        mock: Any,
    ) -> None:
        response = await client.get(
            "/group/me",
            headers={"Authorization": OTHER_USER_NOT_IN_GROUP_AUTHORIZATION},
        )

        assert response.status_code == 200
        assert response.json() == ME_NEW_USER_RESPONSE

        check_response_time(response)

    @pytest.mark.asyncio
    async def test_create_punishment_type_forbidden(self, client: Any) -> None:
        response = await client.post(
            "/group/1/punishmentType",
            json=NEW_PUNISHMENT_TYPE_PAYLOAD,
            headers={"Authorization": OTHER_USER_NOT_IN_GROUP_AUTHORIZATION},
        )
        assert response.status_code == 403
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_create_punsihment_type(self, client: Any) -> None:
        response = await client.post(
            "/group/1/punishmentType",
            json=NEW_PUNISHMENT_TYPE_PAYLOAD,
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        assert response.json() == {"id": 4}
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_group_with_punishment_type(self, client: Any) -> None:
        response = await client.get(f"/group/1")
        assert response.status_code == 200
        assert response.json()["punishment_types"] == DEFAULT_PUNISHMENT_TYPES + [
            WAFFLES_PUNISHMENT_TYPE_RESPONSE
        ]

        check_response_time(response)

    @pytest.mark.asyncio
    async def test_delete_punishment_type_user_not_in_group(self, client: Any) -> None:
        response = await client.delete(
            "/group/1/punishmentType/4",
            headers={"Authorization": OTHER_USER_NOT_IN_GROUP_AUTHORIZATION},
        )
        assert response.status_code == 403
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_delete_punishment_type(self, client: Any) -> None:
        response = await client.delete(
            "/group/1/punishmentType/4",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_create_punishment_on_self_user(self, client: Any) -> None:
        response = await client.post(
            f"/group/1/user/{SELF_USER_ID}/punishment",
            json=[
                {
                    "punishment_type_id": 1,
                    "reason": "Very good reason",
                    "amount": 1,
                }
            ],
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        assert response.json()["ids"] == [1]
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_create_punishment_on_other_user(self, client: Any) -> None:
        response = await client.post(
            f"/group/1/user/{OTHER_USER_ID}/punishment",
            json=[
                {
                    "punishment_type_id": 2,
                    "reason": "Very good reason2",
                    "amount": 1,
                }
            ],
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        assert response.json()["ids"] == [2]
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_create_punishment_on_other_user_not_in_group(
        self,
        client: Any,
    ) -> None:
        response = await client.post(
            f"/group/1/user/{OTHER_USER_NOT_IN_GROUP_ID}/punishment",
            json=[
                {
                    "punishment_type_id": 2,
                    "reason": "Very good reason2",
                    "amount": 1,
                }
            ],
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 400
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_verify_own_punishment(self, client: Any) -> None:
        response = await client.post(
            f"/punishment/1/verify",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 403
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_verify_other_user_punishment(self, client: Any) -> None:
        response = await client.post(
            "/punishment/2/verify",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        assert response.json()["verified_time"] is not None
        check_response_time(response)

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_verify_other_user_punishment_already_verified(
        self,
        client: Any,
    ) -> None:
        response = await client.post(
            "/punishment/2/verify",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 400
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_delete_own_punishment_created_by_other(self, client: Any) -> None:
        response = await client.delete(
            "/punishment/2",
            headers={"Authorization": OTHER_USER_AUTHORIZATION},
        )
        assert response.status_code == 403
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_delete_own_punishment_created_by_self(self, client: Any) -> None:
        response = await client.delete(
            "/punishment/1",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 200
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_delete_own_punishment_created_by_self_duplicate(
        self,
        client: Any,
    ) -> None:
        response = await client.delete(
            "/punishment/1",
            headers={"Authorization": SELF_USER_AUTHORIZATION},
        )
        assert response.status_code == 404
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_check_punishments_exists(self, client: Any) -> None:
        response = await client.get(f"/group/1/user/{OTHER_USER_ID}")
        punishments = response.json()["punishments"]
        assert len(punishments) == 1
        check_response_time(response)

    @pytest.mark.asyncio
    async def test_get_punishment_exists_group_users(self, client: Any) -> None:
        response = await client.get(f"/group/1/users")
        assert response.status_code == 200
        punishments = response.json()[3]["punishments"]
        assert len(punishments) == 1
