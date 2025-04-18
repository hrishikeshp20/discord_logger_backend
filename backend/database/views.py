from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DiscordUser
from .serializers import DiscordUserSerializer

@api_view(["POST"])
def sync_discord_user(request):
    data = request.data
    user_id = data.get("user_id")
    user_name = data.get("user_name")
    status = data.get("status", True)  # True = join, False = leave
    print(data)

    try:
        user = DiscordUser.objects.get(user_id=user_id)





        # Case 1: Join received, user exists, status is True
        if status is True and user.status is True:
            user.join_count += 1
            print("1")

        elif status is True and user.status is False:
            user.join_count += 1
            user.status = status
            print("1")

        elif status is False and user.status is True:
            user.status = status


        # Case 2: Leave received, user exists, status is False
        elif status is False and user.status is False:
            user.join_count += 1
            print("2")


        # Outside your cases: do nothing
        else:
            print("3")

            return Response({"message": "Event ignored — not part of tracked cases."})

    except DiscordUser.DoesNotExist:
        # Case 3: Leave received, user doesn't exist
        if status is False:
            user = DiscordUser.objects.create(
                user_id=user_id,
                user_name=user_name,
                status=status,
                join_count=1
            )
            print("elif")

        elif status is True:
            user = DiscordUser.objects.create(
                user_id=user_id,
                user_name=user_name,
                status=status,
                join_count=1
            )
            print("elif2")
        else:
            return Response({"message": "Event ignored — not part of tracked cases."})

    # Always update name if we're saving
    user.user_name = user_name
    user.save()
    return Response(DiscordUserSerializer(user).data)


@api_view(["POST"])
def bulk_sync_users(request):
    data = request.data  # This will be a list of users

    for item in data:
        user_id = item.get("user_id")
        user_name = item.get("user_name")
        status = item.get("status", True)

        user, created = DiscordUser.objects.get_or_create(user_id=user_id)

        user.user_name = user_name
        user.status = status

        # Initial sync: set join_count to 1 only if user is new
        if created:
            user.join_count = 1

        user.save()

    return Response({"message": f"{len(data)} users synced successfully."})




