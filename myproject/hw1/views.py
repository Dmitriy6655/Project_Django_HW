from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate',
           'Pragma': 'no-cache'}


def index(request):
    body = """
        <title>Главная страница</title>
        <body>
            <div>
                <h1>Мой первый сайт django</h1>
                <p>Содержимое </p>
                <p>Перейдите на страницу: /about</p>
            </div>
            <footer>
                <div>
                    <p>Copyright &copy;
                        <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                        Все права защищены.
                    </p>
                </div>
            </footer>
        </body>
        """
    logger.info('Home page is open.')
    return HttpResponse(body, charset="utf-8", headers=headers)


def about(request):
    body = """
           <title>О себе</title>  
           <body>     
               <div>
                    <h1>О себе</h1>
                   <h2>Силиверстов Тимур Александрович</h2>
                   <p>Мужчина, 29 лет, родился 15 марта  1994</p>
                   <p>Перейдите на страницу: http://127.0.0.1:8000/</p>
               </div>
               <footer>
                   <div>
                       <p>Copyright &copy;
                           <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                           Все права защищены.
                       </p>
                   </div>
               </footer>
           </body>
           """
    logger.info('About page is open.')
    return HttpResponse(body, charset="utf-8", headers=headers)
