def create_check_ins():
    users = User.query.all()
    for user in users:
        num_checkins = random.randint(5, 365)  # 每个用户随机5到365次签到
        dates = [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_checkins)]
        dates = list(set(dates))  # 确保日期唯一
        for date in dates:
            check_in = CheckIn(
                user_id=user.user_id,
                checkin_date=date
            )
            db.session.add(check_in)
    db.session.commit()

