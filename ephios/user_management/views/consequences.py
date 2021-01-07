from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from ephios.user_management.consequences import editable_consequences
from ephios.user_management.models import Consequence


class ConsequenceUpdateView(LoginRequiredMixin, SingleObjectMixin, View):
    def get_queryset(self):
        return editable_consequences(self.request.user)

    def post(self, request, *args, **kwargs):
        consequence = self.get_object()
        if request.POST["action"] == "deny":
            consequence.deny(request.user)
        elif request.POST["action"] == "confirm":
            consequence.confirm(request.user)

        if request.is_ajax():
            return JsonResponse(
                {"state": consequence.state, "fail_reason": consequence.fail_reason}
            )
        if consequence.state == Consequence.States.FAILED:
            messages.error(request, _("There was an error performing that action."))
        return redirect("event_management:index")