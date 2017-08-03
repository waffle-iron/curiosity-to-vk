# -*- coding: utf-8 -*-
import vk_api


def post():
    # Ауторизация
    login, password = '89214447344', 'e31f567b'
    vk_session = vk_api.VkApi(login, password)
    # проверка сессиии
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    # получаем объект API
    vk = vk_session.get_api()
    # получаем файловый объект сессии используемый для загрузки
    upload = vk_api.VkUpload(vk_session)
    # получаем объект конкретной фотографии
    photo = upload.photo('./topics/0.png', album_id=243696878)
    # получаем URI для зармещения фотографии
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )
    # формируем двоичный объект для прикрепления файлов в пост
    attachimg = 'photo{}_{}'.format(photo[0]["owner_id"], photo[0]["id"])
    # ПОСТИМ ВСЕ ЭТО ДЕЛО
    post = vk.wall.post(owner_id=408323065,
                        friends_only = 0,
                        from_group = 0,
                        message="Магия питона в действии ))",
                        attachments= attachimg,
                        lat = 59.946406,
                        long = 30.275867
                        )

if __name__ == '__main__':
    print("posting")
