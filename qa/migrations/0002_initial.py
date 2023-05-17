# Generated by Django 3.2.15 on 2023-05-14 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qa', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reputation',
            name='awarded_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reputation',
            name='question_O',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='qupvote',
            name='upvote_by_q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qupvote',
            name='upvote_question_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='lastActiveFor_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lastActiveFor_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='page_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qa.page_element'),
        ),
        migrations.AddField(
            model_name='question',
            name='post_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='q_edited_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q_edited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='question',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qdownvote',
            name='downvote_by_q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qdownvote',
            name='downvote_question_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='protectquestion',
            name='protected_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='protectquestion',
            name='protecting_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='protectquestion',
            name='protectionRemovedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protectionRemovedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page_element',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_elements', to='qa.page'),
        ),
        migrations.AddField(
            model_name='page',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='qa.page'),
        ),
        migrations.AddField(
            model_name='historicalqupvote',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='qupvotehistory', to='qa.qupvote'),
        ),
        migrations.AddField(
            model_name='historicalqupvote',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalqupvote',
            name='upvote_by_q',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalqupvote',
            name='upvote_question_of',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.question'),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='his', to='qa.question'),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='lastActiveFor_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='page_element',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.page_element'),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='post_owner',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='q_edited_by',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalqdownvote',
            name='downvote_by_q',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalqdownvote',
            name='downvote_question_of',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.question'),
        ),
        migrations.AddField(
            model_name='historicalqdownvote',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='qdownvotehistory', to='qa.qdownvote'),
        ),
        migrations.AddField(
            model_name='historicalqdownvote',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcommentq',
            name='answer_comment',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.answer'),
        ),
        migrations.AddField(
            model_name='historicalcommentq',
            name='commented_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcommentq',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commentHis', to='qa.commentq'),
        ),
        migrations.AddField(
            model_name='historicalcommentq',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcommentq',
            name='question_comment',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.question'),
        ),
        migrations.AddField(
            model_name='historicalbounty',
            name='bounty_awarded_to',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbounty',
            name='by_user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbounty',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bountyhistory', to='qa.bounty'),
        ),
        migrations.AddField(
            model_name='historicalbounty',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbounty',
            name='question_bounty',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.question'),
        ),
        migrations.AddField(
            model_name='historicalanswer',
            name='a_edited_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalanswer',
            name='answer_owner',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalanswer',
            name='history_relation',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='anshis', to='qa.answer'),
        ),
        migrations.AddField(
            model_name='historicalanswer',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalanswer',
            name='questionans',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='qa.question'),
        ),
        migrations.AddField(
            model_name='commentq',
            name='answer_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='commentq',
            name='com_upvote',
            field=models.ManyToManyField(blank=True, related_name='comm_upvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentq',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentq',
            name='question_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='bounty_awarded_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bounty_awarded_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bounty',
            name='by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bounty',
            name='question_bounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='bookmarkquestion',
            name='bookmarked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmarkquestion',
            name='bookmarked_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='banneduser',
            name='banned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banneduser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='com',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='a_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='a_edited_time', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='a_vote_downs',
            field=models.ManyToManyField(blank=True, related_name='a_vote_down', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='a_vote_ups',
            field=models.ManyToManyField(blank=True, related_name='a_vote_up', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
    ]