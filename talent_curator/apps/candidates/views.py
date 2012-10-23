from flask import redirect, render_template, session, g, url_for, request, flash


@candidates_blueprint.route('/list')
def list():
	return render_template('list.html', candidates=[])