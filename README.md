# asyncdjango

A small sample project to profile the performance of asynchronous Python when used in typical Django views.

## Description


To evaluate the performance of async Django views in comparison to traditional sync Django views I created two views:

* a classic sync view
  (see: https://github.com/antonpirker/asyncdjango/blob/main/app/views.py#L21)

* and an async view.
  (see: https://github.com/antonpirker/asyncdjango/blob/main/app/views.py#L36)

Both views make two simple queries to the database:
* one query fetching a list of items and
* the second query fetching the details of one item.

I have used `asyncpg` in the async view and have used `psycopg2` in the sync view (without using the ORM of Django for better comparison, because there is async ORM yet).

Then I have run the project once in Gunicorn with the default sync workers to see how long the views take when running in a synchronous Gunicorn process.

    You can try the project with sync Gunicorn here:
    https://30d2782–antonpirker-asyncdjango.wdpr.run/

I also have run the project in Gunicorn but using the Uvicorn async workers to see how long the views take when running a asynchronous Uvicorn process.

    You can try the project with async Uvicorn here:
    https://5f7f888–antonpirker-asyncdjango.wdpr.run/ 1

(You can also look at the server output when you click on the “Logs” button in the widget on the lower right of the page. You need to be authenticated with your GitHub account to see the logs)

## Load testing on local machine

I ran both views in a Docker container connecting to Postgres also in a Docker container on my AMD CPU with 8 cores.

### This is the sync view running in out of the box Gunicorn:

Here the moment when the slow down of the view starts: (at ~130 concurrent users)
[!Sync View With Sync Workers Slowdown](documentation/screenshots/sync-view-sync-workers-slowdown.png)

And this is when the view starts to throw errors: (at ~310 concurrent users)
[!Sync View With Sync Workers Errors](documentation/screenshots/sync-view-sync-workers-erros.png)

### This is the same for the async view running in Uvicorn workers in Gunicorn.

(Like the [Uvicorn documentation](https://www.uvicorn.org/deployment/) tells me that Uvicorn should be run in production)

When the slow down of the view starts: (at ~100 concurrent users)
[!Async View With Async Workers Slowdown](documentation/screenshots/async-view-async-workers-slowdown.png)

When the errors start: (at ~280 concurrent users)
[!Async View With Async Workers Errors](documentation/screenshots/async-view-async-workers-erros.png)


## Conclusion

I can not see substantial performance gains when using async database queries in Django views.

So until there is no full async ORM and you only make database queries and do not load data over HTTP from a third party API in your views, it is not worth the efford to change your views to async yet.

As the User [KenWithsell in a comment the Django Forum points out](https://forum.djangoproject.com/t/evaluation-of-performance-of-async-views-they-suck/8788/), this will probably be due to Postgres everything memory resident. (Because it is only a tiny database, that can fit in memory easily)