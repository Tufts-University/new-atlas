from django.db import models


class Dictionary(models.Model):
    """
    A dictionary model.
    """

    label = models.CharField(blank=True, null=True, max_length=255)
    data = models.JSONField(default=dict, blank=True)

    urn = models.CharField(max_length=255, unique=True, help_text="urn:cite2:&lt;site>:dictionaries.atlas_v1")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Dictionaries"

    # def senses(self):
    #     return Sense.objects.filter(entry__dictionary=self)

    # def citations(self):
    #     return Citation.objects.filter(entry__dictionary=self)
    
    def first_entry(self):
        return self.entries.order_by("idx").first()


class DictionaryEntry(models.Model):
    headword = models.CharField(max_length=255, db_index=True)
    headword_normalized = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    headword_normalized_stripped = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    data = models.JSONField(default=dict, blank=True)

    idx = models.IntegerField(help_text="0-based index")
    urn = models.CharField(max_length=255, unique=True, help_text="urn:cite2:&lt;site>:entries.atlas_v1")
    dictionary = models.ForeignKey(Dictionary, related_name="entries", on_delete=models.CASCADE)

    def __str__(self):
        return self.headword

    class Meta:
        verbose_name_plural = "Dictionary Entries"
        unique_together = ("dictionary", "idx")

    def previous_entries(self, count):
        return DictionaryEntry.objects.filter(dictionary=self.dictionary, idx__lt=self.idx).order_by("-idx")[:count:-1]
    
    def next_entries(self, count):
        return DictionaryEntry.objects.filter(dictionary=self.dictionary, idx__gt=self.idx).order_by("idx")[:count]


# class Sense(MP_Node):
#     label = models.CharField(blank=True, null=True, max_length=255)
#     definition = models.TextField(blank=True, null=True)

#     alphabet = settings.SV_ATLAS_TREE_PATH_ALPHABET

#     idx = models.IntegerField(help_text="0-based index", blank=True, null=True)
#     urn = models.CharField(max_length=255, unique=True, help_text="urn:cite2:&lt;site>:senses.atlas_v1")

#     entry = models.ForeignKey(DictionaryEntry, related_name="senses", on_delete=models.CASCADE)


# class Citation(models.Model):
#     label = models.CharField(blank=True, null=True, max_length=255)
#     idx = models.IntegerField(help_text="0-based index", blank=True, null=True)
#     urn = models.CharField(max_length=255, unique=True, help_text="urn:cite2:&lt;site>:citations.atlas_v1")
#     entry = models.ForeignKey(DictionaryEntry, blank=True, null=True, related_name="citations",on_delete=models.CASCADE)
#     sense = models.ForeignKey(Sense, blank=True, null=True, related_name="citations", on_delete=models.CASCADE)
#     data = models.JSONField(default=dict, blank=True)

#     # TODO: There may be additional optimizations we can do on the text part / citation relation
#     # TODO: Higher-order URNs?
#     # text_parts = SortedManyToManyField(Node, related_name="sense_citations")
