from django.contrib import admin, messages
from django.shortcuts import get_object_or_404, redirect, render, resolve_url as r
from django.utils.translation import ngettext

from bible.core.models import Lection, Versicle


@admin.action(description='Incluir versículos')
def include_versicles(modeladmin, request, queryset):
    context = dict(
        modeladmin.admin_site.each_context(request),
        title='Incluir versículos na leitura',
        queryset=queryset,
        lections=Lection.objects.all(),
        action_name='include_versicles',
    )

    if request.POST.get('post'):
        try:
            lection = get_object_or_404(Lection, order=request.POST.get('lection'))

            for obj in queryset:
                obj.lection = lection

            Versicle.objects.bulk_update(queryset, ['lection'])
            modeladmin.message_user(request, ngettext(
                '%d versículo foi incluído na leitura %s.',
                '%d versículos foram incluídos na leitura %s.',
                len(queryset),
            ) % (len(queryset), lection.order), messages.SUCCESS)

            return redirect(r('admin:core_versicle_changelist'))

        except:
            modeladmin.message_user(
                request, 'Nenhum versísculo foi incluído.', messages.ERROR)

            return render(request, 'admin/include_versicles.html', context)


    return render(request, 'admin/include_versicles.html', context)
