from django.contrib import admin
from .models import All_Area, TreeKind, Tree, Area, Group, Owner

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Tree),
admin.site.register(Owner),
admin.site.register(Group),
admin.site.register(TreeKind, SlugAdmin)
admin.site.register(Area)
admin.site.register(All_Area, SlugAdmin)


