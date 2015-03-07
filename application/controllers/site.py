# coding: utf-8
from datetime import date, timedelta
from flask import render_template, Blueprint
from ..models import db, Piece

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """Index page."""
    today = date.today()
    today_pieces = get_pieces_by_day(today)
    yesterday = today - timedelta(days=1)
    yesterday_pieces = get_pieces_by_day(yesterday)
    the_day_before_yesterday = today - timedelta(days=2)
    the_day_before_yesterday_pieces = get_pieces_by_day(the_day_before_yesterday)
    return render_template('site/index.html', today_pieces=today_pieces,
                           yesterday_pieces=yesterday_pieces,
                           the_day_before_yesterday=the_day_before_yesterday,
                           the_day_before_yesterday_pieces=the_day_before_yesterday_pieces)


def get_pieces_by_day(day):
    """获取某天的pieces"""
    return Piece.query.filter(db.func.date(Piece.created_at) == day).order_by(
        Piece.votes_count.desc()).limit(15)


@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about.html')