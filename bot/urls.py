from bot import views
from django.urls import path

urlpatterns = [
    path("branches", views.BranchListAPI.as_view(), name="branch_list"),
    path(
        "branch/<int:id>/semisters",
        views.SemisterBranchListAPI.as_view(),
        name="semister_branch",
    ),
    path(
        "branch/<int:branchId>/semister/<int:semisterId>/subjects",
        views.BranchSemisterSubjectListAPI.as_view(),
        name="semister_branch",
    ),
    path(
        "branch/<int:branchId>/semister/<int:semisterId>/subject/<int:subjectId>/documents",
        views.BranchSemisterSubjectDocumentListAPI.as_view(),
        name="semister_branch",
    ),
]
