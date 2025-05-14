# Ev Işık Simülasyonu

Bu uygulama, bir evin odalarının ışıklarını kontrol etmek için kullanılan bir web simülasyonudur. Flask kullanarak arka planda çalışır ve odaların ışıklarını açıp kapatmak için bir API sunar.

## Özellikler

- 6 farklı oda (salon, oturma odası, mutfak, tuvalet, banyo, yatak odası)
- Her oda için ışık kontrolü
- Tüm ışıkları açma/kapatma düğmeleri
- REST API ile ışık kontrolü

## Kurulum

1. Gereksinimleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

2. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

3. Tarayıcınızdan `http://localhost:5004` adresine erişin

## API Kullanımı

Işıkları kontrol etmek için aşağıdaki API'yi kullanabilirsiniz:

```
POST /api/lights
Content-Type: application/json

{
  "room": "oda_adı",
  "lights": true/false
}
```

Örnek:
```
{
  "room": "tuvalet",
  "lights": true
}
```

### Curl ile API Kullanım Örnekleri:

Tuvalete ait ışığı açmak için:
```bash
curl -X POST http://localhost:5004/api/lights \
  -H "Content-Type: application/json" \
  -d '{"room": "tuvalet", "lights": true}'
```

Salona ait ışığı kapatmak için:
```bash
curl -X POST http://localhost:5004/api/lights \
  -H "Content-Type: application/json" \
  -d '{"room": "salon", "lights": false}'
```

## Tüm oda durumlarını almak için:

```
GET /api/get_states
```

Curl ile tüm oda durumlarını almak için:
```bash
curl -X GET http://localhost:5004/api/get_states
```

## Gerçek Zamanlı Güncelleme

Bu uygulama WebSocket (socket.io) kullanarak API üzerinden yapılan değişiklikleri anlık olarak web arayüzünde gösterir. API ile yapılan her güncelleme, sayfayı yenilemeye gerek kalmadan otomatik olarak web arayüzünde güncellenir.
