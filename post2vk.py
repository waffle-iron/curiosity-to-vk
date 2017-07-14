# -*- coding: utf-8 -*-
import vk_api


def post():
    """ Пример поста с текстом и фото """

    login, password = '89214447344', 'e31f567b'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """
    vk = vk_session.get_api()

    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo('./topics/0.png', album_id=243696878)

    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )

    attachimg = 'photo{}_{}'.format(photo[0]["owner_id"], photo[0]["id"])

    post = vk.wall.post(owner_id=408323065,
                        friends_only = 0,
                        from_group = 0,
                        message="Магия питона в действии ))",
                        attachments= attachimg,
                        lat = 59.946406,
                        long = 30.275867
                        )

    print('\nLink: ', vk_photo_url, '\nPost: ', vk.response.post)
post()
if __name__ == '__main__':
    print("posting")
