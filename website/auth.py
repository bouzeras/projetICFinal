from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User, Groupe
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

##################### Crée un compte ############################################################
@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')
        
        #if userName == "admin":
      # Check if the username already exists in the database
        user = User.query.filter_by(user_name=userName).first()
        if user:
            flash('Le nom d\'utilisateur existe déjà, veuillez en choisir un autre.', category='error')
            return redirect(url_for('auth.sign_up'))
        else:
            new_user = User(user_name=userName, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Le compte a été créé avec succès !', category='success')
            #return redirect(url_for('groupeU.join_group', invitation_code="ABC123"))
            return redirect(url_for('groupeU.home'))
    return render_template("sign_up.html", user=current_user)

############################# Se connecter ####################################################
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')

        user = User.query.filter_by(user_name=userName).first()
        if user:
              """
            # verifier le mot de passe
            if check_password_hash(user.password, password):
              """
        flash('Connexion réussie !', category='success')
        login_user(user, remember=True)
        #return redirect(url_for('groupeU.join_group', invitation_code="ABC123"))
        return redirect(url_for('groupeU.home'))
        """
            else:
                flash('Mot de passe incorrect.', category='error')
             """
    else:
            flash('L\'utilisateur n\'existe pas.', category='error')
    return render_template("login.html", user=current_user)
  #data = request.form
    #print(data)

##################################### Se deconnecter ############################################
@auth.route('/logout')
@login_required #si on est pas connecté, on ne peut pas se déconnecter
def logout():
#on se déconnecte
    logout_user()
    return redirect(url_for('auth.login'))



######################################## Liste des utilisateurs ###########################################
def join_group(request):
    if request.method == 'POST':
        groupe_id = request.POST['groupe']
        try:
            groupe = Groupe.objects.get(id=groupe_id)
        except Groupe.DoesNotExist:
            messages.error(request, 'Groupe introuvable ou mot de passe incorrect.')
            return redirect('join_group')

        membre = member(user=request.user, groupe=groupe)
        membre.save()
        group_members = MemberDescriptorType.objects.filter(groupe=groupe).select_related('user')
        context = {
            'groupe': groupe,
            'group_members': group_members
        }
        return render_template(request, 'home.html', context)

    return render_template(request, 'home.html')
"""
#retourne la liste des utilisateurs d'un groupe
@auth.route('/groupe', methods=['GET','POST'])
@login_required
def groupe():
    users = User.query.filter_by(groupe=current_user.groupe).all()
    return render_template("groupe.html", users=users, current_user=current_user)
"""
