# sql-workshop

This is material for [Hashrocket][hr]'s SQL workshop at [Code Platoon][cp].

At Hashrocket, we 💙 SQL! This engagement has given us many opportunities to
share that passion, in a practical and hands-on way, with the veterans and
spouses of Code Platoon.

Check out the [Agenda][agenda] to see how the day will progress.

### Setup

Clone the repo:

```
$ git clone https://github.com/jwworth/sql-workshop
```

Install [PostgreSQL][pg]. This is really important; please try to have a
working PostgreSQL REPL ready before we begin!

One way to verify a working Postgres installation would be to create and
connect to a Postgres database.

```
$ createdb deleteme
$ psql deleteme

psql (13.4)
Type "help" for help.

deleteme=# exit

$ dropdb deleteme
```

We'll start with the Phone Book domain.

```
$ cd sql-workshop/phone_book
```

Open up the `lesson.sql` in your text editor.

### Additional Resources

You can't beat the official [PostgreSQL docs][pg-docs]. They are about as good
as documentation gets. This [conventions page][pg-conventions] will help you
read them.

From us, we're proud to have contributed [PG Casts][pgcasts]. This series of
videos covers in greater detail many of the commands we'll teach today.

### License

This project is released under the [MIT License][mit].

### Sponsor

[![Hashrocket logo](https://hashrocket.com/hashrocket_logo.svg)](https://hashrocket.com)

This workshop is supported by the team at [Hashrocket, a multidisciplinary
design and development consultancy](https://hashrocket.com). If you'd like to
[work with us](https://hashrocket.com/contact-us/hire-us) or [join our
team](https://hashrocket.com/contact-us/jobs), don't hesitate to get in touch.

<a href="https://www.ccsalespro.com/"><img alt="CCSalesPro logo" src="https://www.ccsalespro.com/wp-content/uploads/2016/04/CCSales-Pro-Logo-Beveled-50.png" height="100">
</a>

This workshop is also supported by [CCSalesPro](https://www.ccsalespro.com/),
a provider of training and technology for the merchant services industry.

[agenda]: agenda.md
[cp]: https://www.codeplatoon.org/
[hr]: https://hashrocket.com/
[mit]: http://www.opensource.org/licenses/MIT
[pg-conventions]: https://www.postgresql.org/docs/current/notation.html
[pg-docs]: https://www.postgresql.org/docs/
[pg]: https://www.postgresql.org/
[pgcasts]: https://pgcasts.com/
