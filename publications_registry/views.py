from django.shortcuts import render
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)


# Create your views here.
class OverviewView(View):
    """
    Displays database.
    """
    def get(self, request):
        return render(request,
                      "publications_registry/overview.html")


class RecordCreateView(CreateView):
    """
    Creates a new record in the database.
    """
    pass


class RecordDisplayView(DetailView):
    """
    Displays detailed view of a record.
    """


class RecordUpdateView(UpdateView):
    """
    Updates a record in the database.
    """
    pass


class RecordDeleteView(DeleteView):
    """
    Deletes a record in the database.
    """
    pass
