from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/memberbucks/transactions/",
        views.MemberBucksTransactions.as_view(),
        name="MemberBucksTransactions",
    ),
    path(
        "api/memberbucks/balance/",
        views.MemberBucksBalance.as_view(),
        name="MemberBucksBalance",
    ),
    path(
        "api/memberbucks/card/",
        views.MemberBucksAddCard.as_view(),
        name="MemberBucksAddCard",
    ),
    path(
        "api/memberbucks/add/<int:amount>/",
        views.MemberBucksAddFunds.as_view(),
        name="MemberBucksAddFunds",
    ),
]