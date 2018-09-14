
# Twitter Spammer

Yine bir dönem farklı bir grup için geliştirdiğim bu araç ile elinizde ki hesapları kullanarak belirlediğiniz hesaplara spam saldırısı yapabilirsiniz. Aktif proxy değiştirdiğinden yakalanma riski oldukça azdır.


# Kurulum

Kurulum için "**git**" sistemi kullanılabilir.
```sh
~$ git clone https://github.com/MuReCoder/twspammer.git .
```

## Bağımlılıklar

Program çeşitli bağımlılıklara sahiptir, bu bağımlılıklar sağlanmadan çalışmayacaktır. Bağımlılıkları **pip** ile yükleyebilirsiniz.

```sh
~$ pip install ragent
~$ pip install mechanize
~$ pip install requests
```

## Kullanım

Python2 ile geliştirilen programı **python twspammer.py** diyerek çalıştırabilirsiniz. Daha sonra komut satırından **help** diyerek yardım menüsüne ulaşabilirsiniz.

![
](https://emregeldegul.net/wp-content/uploads/2018/09/twspam.png)

**Not:** proxy güncellemesi yapmadan spam işlemini başlatmayın.

```sh
~$ update proxy
```
Artık **spam kullaniciAdi** diyerek spam işlemine başlayabilirsiniz.

![
](https://emregeldegul.net/wp-content/uploads/2018/09/twSpamEx.png)

Sizden istenen ID aralığını elinizd ki user liste göre vererek spam işlemini başlatabilirsiniz.

## Kullanıcı Tanımlama
**accounts.json** dosyasına JSON formatında kullanıcıları ekleyebilirsiniz.
