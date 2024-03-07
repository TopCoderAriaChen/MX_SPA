db.createUser({
  user: 'api',
  pwd: 'password',
  roles: [
    {
      role: 'readWrite',
      db: 'app'
    }
  ]
});
