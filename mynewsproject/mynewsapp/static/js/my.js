//alert('Hello Js!');


//var button = document.querySelector("#btn-joke");
////console.log(button);
//
//function foo(event)
//{
//    element = event.target;
//
//    if ( element.classList.contains('btn-info') )
//    {
//        var new_class = 'btn-danger';
//        var old_class = 'btn-info';
//    }
//    else {
//        var new_class = 'btn-info';
//        var old_class = 'btn-danger';
//    }
//
//    element.classList.remove(old_class);
//    element.classList.add(new_class);
//}
//
//button.addEventListener('click', foo, false);
//
//// ajax
//$( document ).on('click', '#ajax-btn', function(event) {
//    console.log('Step 1');
//    $.ajax({
//                url: '/users/update-token-ajax/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    console.log('Step 3')
//                    console.log(data);
//                    $('#token').html(data.key);
//                },
//            });
//});

$(document).ready(function() {
    // Обработчик события для кнопки "Все"
    $(document).on('click', '#all', function(event) {
        $.ajax({
            url: '/api/v0/allnews/',
            success: function (data) {
                console.log('Step 3');
                console.log(data);

                $('#div_allnews').empty(); // Очищаем содержимое списка перед добавлением новых элементов

                if (Array.isArray(data) && data.length > 0) {
                    // Проверяем, что данные представляют собой непустой массив
                    for (let i = 0; i < data.length; i++) {
                        const item = data[i];
                        // Проверяем, что у каждого элемента есть поле "title"
                        if (item.hasOwnProperty('title')) {
                            const title = item.title;
                            console.log(title);
                            $('#div_allnews').append('<li>' + title + '</li>');
                        } else {
                            console.warn('Element is missing the "title" field:', item);
                        }
                    }
                } else {
                    console.warn('Received empty or non-array data:', data);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('AJAX request failed:', textStatus, errorThrown);
            }
        });
    });

    // Обработчик события для кнопки "Посты"
    $(document).on('click', '#posts', function(event) {
        $.ajax({
            url: '/api/v0/posts/',
            success: function(data) {
                console.log('Step 3');
                console.log(data);

                $('#div_posts').empty(); // Очищаем содержимое списка перед добавлением новых элементов

                if (Array.isArray(data) && data.length > 0) {
                    // Проверяем, что данные представляют собой непустой массив
                    for (let i = 0; i < data.length; i++) {
                        const item = data[i];
                        // Проверяем, что у каждого элемента есть поле "title"
                        if (item.hasOwnProperty('title')) {
                            const title = item.title;
                            console.log(title);
                            $('#div_posts').append('<li>' + title + '</li>');
                        } else {
                            console.warn('Element is missing the "title" field:', item);
                        }
                    }
                } else {
                    console.warn('Received empty or non-array data:', data);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('AJAX request failed:', textStatus, errorThrown);
            }
        });
    });

});







