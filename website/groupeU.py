from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import current_user, login_required
from .models import User, Groupe
from . import db
import json

groupeU = Blueprint('groupeU', __name__)

############################################ Acceuil ################################################################
@groupeU.route('/', methods=['GET','POST'])
@login_required
def home():
    """
    if request.method == 'POST':
        groupe = request.form.get('groupe')
        if len(Groupe) < 1:
            flash('Pas de groupe', category='error')
        else:
            new_groupe = Groupe(data=groupe, user_id=current_user.id)
            db.session.add(new_groupe)
            db.session.commit()
            flash('Groupe added!', category='success')
            """
    return render_template("home.html", user=current_user)

######################################## Ajouter un utilisateur dans un groupe ###########################################
    """
@groupeU.route('/join-group/<invitation_code>', methods=['GET','POST'])
@login_required
def join_group(invitation_code):
    group = Groupe.query.filter_by(invitation_code=invitation_code).first()
    if not group:
        flash('Code d\'invitation invalide.', category='error')
        return redirect(url_for('home'))
    if len(group.users) >= group.max_users:
        flash('Le groupe est complet.', category='error')
        return redirect(url_for('home'))
    current_user.groupe = group
    db.session.commit()
    flash('Vous avez rejoint le groupe avec succès!', category='success')
    return redirect(url_for('show_group', group_id=group.id))

@groupeU.route('/join-random-group', methods=['GET','POST'])
@login_required
def join_random_group():
    groups = Groupe.query.all()
    for group in groups:
        if len(group.users) < group.max_users:
            if current_user.groupe != group:
                current_user.groupe = group
                db.session.commit()
                flash('Vous avez été ajouté au groupe {} avec succès!'.format(group.name), category='success')
                return redirect(url_for('show_group', group_id=group.id))
    nb_groups = len(groups)
    nb_users = len(User.query.filter_by(groupe=None).all())
    if nb_users % nb_groups == 0:
        last_groupe_max = False
    else:
        if app.config['LAST_GROUP_CONFIG'] == 'LAST_MIN':
            last_groupe_max = False
        elif app.config['LAST_GROUP_CONFIG'] == 'LAST_MAX':
            last_groupe_max = True
    if last_groupe_max:
        max_users_last_group = (nb_users // nb_groups) + 1
    else:
        max_users_last_group = nb_users // nb_groups
    new_groupe = Groupe(name=f"Groupe {nb_groups+1}", max_users=max_users_last_group)
    db.session.add(new_groupe)
    db.session.commit()
    current_user.groupe = new_groupe
    db.session.commit()
    flash('Vous avez été ajouté au nouveau groupe {} avec succès!'.format(new_groupe.name), category='success')
    return redirect(url_for('show-group', group_id=new_groupe.id))

######################################## Affichier les membre d'un groupe ###########################################
@groupeU.route('/show-group/<group_id>', methods=['GET','POST'])
@login_required
def show_group(group_id):
    group = Groupe.query.get(group_id)
    if not group:
        flash('Groupe introuvable.', category='error')
        return redirect(url_for('show_group'))
    users = group.users
    return render_template('group.html', user=current_user, group=group, users=users)

"""


"""
@groupeU.route('/delete-groupe', methods=['POST'])
def delete_groupe():
    groupe = json.loads(request.data)
    groupeId = groupe['groupeId']
    groupe = Groupe.query.get(groupeId)
    if groupe:
        if groupe.user_id == current_user.id:
            db.session.delete(groupe)
            db.session.commit()
            return jsonify({})
"""