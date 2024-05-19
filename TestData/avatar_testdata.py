def create_avatars(num_avatars=10):
    for i in range(num_avatars):
        avatar = Avatar(
            filename=f'avatar_{i}.jpg',
            path=f'/static/profile-pictures/avatar_{i}.jpg'
        )
        db.session.add(avatar)
    db.session.commit()

