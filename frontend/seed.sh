for i in {1..100}
do
    curl http://127.0.0.1:80/
done
for i in {1..10}
do
    curl http://127.0.0.1:80/foo
done
for i in {1..10}
do
    curl http://127.0.0.1:80/bar
done

