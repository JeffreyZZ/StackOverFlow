# Generated by Django 3.2.15 on 2023-05-14 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qa', '0001_initial'),
        ('review', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewquestionreopenvotes',
            name='reopen_reviewed_by',
            field=models.ManyToManyField(related_name='reopen_reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewquestionreopenvotes',
            name='review_of',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='review.reopenquestionvotes'),
        ),
        migrations.AddField(
            model_name='reviewquestionedit',
            name='answer_to_view_if',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='reviewquestionedit',
            name='edit_reviewed_by',
            field=models.ManyToManyField(related_name='edit_reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewquestionedit',
            name='question_to_view',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='reviewquestionedit',
            name='queue_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.questioneditvotes'),
        ),
        migrations.AddField(
            model_name='reviewlowqualityposts',
            name='is_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='reviewlowqualityposts',
            name='is_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='reviewlowqualityposts',
            name='review_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.lowqualitypostscheck'),
        ),
        migrations.AddField(
            model_name='reviewlowqualityposts',
            name='reviewers',
            field=models.ManyToManyField(related_name='reviewers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewflagpost',
            name='flag_answer_to_view_if',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='reviewflagpost',
            name='flag_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='review.flagpost'),
        ),
        migrations.AddField(
            model_name='reviewflagpost',
            name='flag_question_to_view',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='reviewflagpost',
            name='flag_reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewflagcomment',
            name='c_flag_reviewed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewflagcomment',
            name='flag_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.commentq'),
        ),
        migrations.AddField(
            model_name='reviewflagcomment',
            name='review_of',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='review.flagcomment'),
        ),
        migrations.AddField(
            model_name='reviewclosevotes',
            name='question_to_closed',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='reviewclosevotes',
            name='review_of',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='review.closequestionvotes'),
        ),
        migrations.AddField(
            model_name='reviewclosevotes',
            name='reviewed_by',
            field=models.ManyToManyField(related_name='reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reopenquestionvotes',
            name='question_to_opening',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='reopenquestionvotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questioneditvotes',
            name='edit_suggested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questioneditvotes',
            name='edited_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='questioneditvotes',
            name='edited_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='lowqualitypostscheck',
            name='low_ans_is',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='lowqualitypostscheck',
            name='low_is',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='lowqualitypostscheck',
            name='suggested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lateanswerreview',
            name='L_AnswerReviewdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lateanswerreview',
            name='L_answerReview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='flagpost',
            name='answer_forFlag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='flagpost',
            name='flagged_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flagpost',
            name='question_forFlag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='flagcomment',
            name='comment_flagged_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flagcomment',
            name='comment_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.commentq'),
        ),
        migrations.AddField(
            model_name='firstquestionreview',
            name='QuestionReviewBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firstquestionreview',
            name='questionReview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='firstanswerreview',
            name='AnswerReviewedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firstanswerreview',
            name='answerReview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.answer'),
        ),
        migrations.AddField(
            model_name='closequestionvotes',
            name='question_to_closing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
        migrations.AddField(
            model_name='closequestionvotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
