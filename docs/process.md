![Image](https://raw.githubusercontent.com/kbalko/flask_blog_app/master/docs/pipeline.PNG)

# Opis procesu

### Po zmianie kodu lokalnie na komputerze:

      #do repo gita
      $git add --all
      $git commit -m"komentarz"
      $git push

Pliki będące na komputerze lokalnie trafiają do repozytorium gita, stąd trafiają do Jenkinsa i Travis CI.

     # do gitlaba
     $ git push gitlab master

Po tej komendzie pliki trafiają do GitLaba.

### Proces testów

Travis/Gitlab/Jenkis sprawdzają zgodność zależności z plików requirements.txt i test_requirements.txt. Następnie uruchamiane są testy jednostkowe, metryki pokrycia kodu i testy w Robot Framework. Po skryptach testowych na podstawie metryk pokrycia kodu uruchamiane jest narzędzie [Coveralls](https://coveralls.io/github/kbalko/flask_blog_app). Proces testów szerzej opisany jest w pliku /docs/proces_todo.md.

### Jenkins - 127.0.0.1:8080


      # instrukcja uruchomienia
      $ cat README.md

      $ git clone https//github.com/kbalko/se_teaching_jenkins
      $ make bulid_jenkins
      $ make run_jenkins

### Docker

Następnie dzięki odpowiednim targetom zawartym pliku Makefile  i dzięki plikom konfiguracyjnym budowany jest Docker, po zbudowaniu następuje push kontenera na hub.docker.com.

      # tergety w Makefile
      $ make docker_build
      $ make docker_run
      $ make docker_stop
      $ make docker_push

 Kontener Dockera: https://hub.docker.com/r/kbalko/hello-world-printer

 ### Heroku
 Następuje deploy aplikacji na Heroku. Aplikcja dostępna pod [linkiem](https://microflaskapp.herokuapp.com/).
