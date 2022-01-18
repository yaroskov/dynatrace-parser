pattern = {
    "source": "",
    "target": "",
    "pseudo": "",
    "task": {
        "key": "",
        "date": "",
        "summary": "",
        "service": ""
    }
}

errors = [
    {
        "source": "На экране s28 не найдено экранов для перехода",
        "target": "На экране s28 не найдено экранов для перехода",
        "pseudo": "На экране s28 не найдено экранов для перехода",
        "task": {
            "key": "EPGUCORE-82521",
            "date": "18.01.2022",
            "summary": "Ошибка при подаче заявления по \"Заявление о выдаче сертификата на материнский (семейный) капитал\"",
            "service": ""
        }
    },
    {
        "source": "На экране s3_al10_1 найдено более 1 экрана для перехода s3_al10_rf,s3_al10_rf",
        "target": "На экране s3_al10_1 найдено более 1 экрана для перехода s3_al10_rf,s3_al10_rf",
        "pseudo": "На экране s3_al10_1 найдено более 1 экрана для перехода s3_al10_rf,s3_al10_rf",
        "task": {
            "key": "EPGUCORE-85189",
            "date": "18.01.2022",
            "summary": "ЕПГУ 2.0 [600349] На экране s3_al10_1 найдено более 1 экрана для перехода s3_al10_rf,s3_al10_rf",
            "service": "600349"
        }
    },
    {
        "source": "На экране s25_2 не найдено экранов для перехода",
        "target": "На экране s25_2 не найдено экранов для перехода",
        "pseudo": "На экране s25_2 не найдено экранов для перехода",
        "task": {
            "key": "EPGUCORE-82767",
            "date": "18.01.2022",
            "summary": "ЕПГУ 2.0 [600127] На экране s25_2 не найдено экранов для перехода",
            "service": "600127"
        }
    },
    {
        "source": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"BAD_REQUEST\",\"message\":\"Bad Request\",\"description\":\"Unexpected server error: Query; CQL [com.datastax.oss.driver.internal.core.cql.DefaultSimpleStatement@154f44fb",
        "target": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"BAD_REQUEST\",\"message\":\"Bad Request\",\"description\":\"Unexpected server error: Query; CQL [com.datastax.oss.driver.internal.core.cql.DefaultSimpleStatement@",
        "pseudo": "Response code: 400 Bad Request - Unexpected server error"
    },
    {
        "source": "Error response from external service. Response code: 500 Internal Server Error. Body: [], url: [http://p00pgunlbservices/internal/api/delirium/2/epgu2service/stages/calc/1713357190], method: [GET]",
        "target": "Error response from external service. Response code: 500 Internal Server Error. Body: [], url: [http://p00pgunlbservices/internal/api/delirium/2/epgu2service/stages/calc/[[target]]], method: [GET]",
        "pseudo": "Response code: 500 Internal Server Error"
    },
    {
        "source": "External entity not found. Response code: 404 Not Found. Body: [], url: [http://p00pgulkapinlb/api/lk/v1/orders/1606348166], method: [GET]",
        "target": "External entity not found. Response code: 404 Not Found. Body: [], url: [http://p00pgulkapinlb/api/lk/v1/orders/[[target]]], method: [GET]",
        "pseudo": "404 ошибка GET запроса к ЛК"
    },
    {
        "source": "Заявление 1719537959 не является черновиком",
        "target": "Заявление [[target]] не является черновиком",
        "pseudo": "Заявление ****** не является черновиком"
    },
    {
        "source": "Ошибка при проверке дублирующихся значений в заявлении. Error response from external service. Response code: 400 Bad Request. Body: [{\"code\":\"FIELD\",\"limitationField\":{\"types\":[],\"orderId\":1697026464,\"checkValues\":[{\"q2-1\":\"Только меня\"},{\"q2-2\":\"Мен",
        "target": "Ошибка при проверке дублирующихся значений в заявлении. Error response from external service. Response code: 400 Bad Request. Body: [{\"code\":\"FIELD\",\"limitationField\":{\"types\":[],\"orderId\":[[target]],\"checkValues\":",
        "pseudo": "Ошибка при проверке дублирующихся значений в заявлении"
    },
    {
        "source": "GepsId: 2931171830 использован в заявке: 1648269764",
        "target": "GepsId: [[target]] использован в заявке: [[target]]",
        "pseudo": "GepsId: ****** использован в заявке: ******"
    },
    {
        "source": "External entity not found. Response code: 404 Not Found. Body: [], url: [http://p00pgulkapinlb/lk-api/internal/api/lk/v1/orders/1725446675/set/attributes], method: [POST]",
        "target": "External entity not found. Response code: 404 Not Found. Body: [], url: [http://p00pgulkapinlb/lk-api/internal/api/lk/v1/orders/[[target]]/set/attributes], method: [POST]",
        "pseudo": "Ошибка 404 в POST запросе к ЛК"
    },
    {
        "source": "Должно возвращаться всегда единственное подразделение по окато 71244, а не нашли ничего.",
        "target": "Должно возвращаться всегда единственное подразделение по окато [[target]], а не нашли ничего.",
        "pseudo": "Должно возвращаться всегда единственное подразделение по окато ******, а не нашли ничего.",
        "task": {
            "key": "EPGUCORE-84542",
            "date": "",
            "summary": "ЕПГУ 2.0 [600109] Должно возвращаться всегда единственное подразделение по окато 71244, а не нашли ничего"
        }
    },
    {
        "source": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"Bad Request\",\"message\":\"BAD_REQUEST\",\"description\":\"Ошибка запроса статуса об отправке в ведомство. Body: IpshStatusDto(super=IpshRequestDto(super=BaseResponse(er",
        "target": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"Bad Request\",\"message\":\"BAD_REQUEST\",\"description\":\"Ошибка запроса статуса об отправке в ведомство. Body: IpshStatusDto(super=IpshRequestDto(super=BaseResponse(er",
        "pseudo": "Ошибка запроса статуса об отправке в ведомство"
    },
    {
        "source": "Index 0 out of bounds for length 0",
        "target": "Index [[target]] out of bounds for length [[target]]",
        "pseudo": "Index ****** out of bounds for length ******"
    },
    {
        "source": "java.lang.IllegalArgumentException: Cannot construct instance of `ru.gosuslugi.pgu.components.descriptor.types.FullAddress` (although at least one Creator exists): no String-argument constructor/factory method to deserialize from String value ('34671",
        "target": "java.lang.IllegalArgumentException: Cannot construct instance of `ru.gosuslugi.pgu.components.descriptor.types.FullAddress` (although at least one Creator exists): no String-argument constructor/factory method to deserialize from String value",
        "pseudo": "Cannot construct instance of `ru.gosuslugi.pgu.components.descriptor.types.FullAddress`"
    },
    {
        "source": "ru.gosuslugi.pgu.common.esia.search.exception.MultiplePersonFoundException: Найдено несколько пользователей с одинаковыми уникально идентифицирующими данными",
        "target": "ru.gosuslugi.pgu.common.esia.search.exception.MultiplePersonFoundException: Найдено несколько пользователей с одинаковыми уникально идентифицирующими данными",
        "pseudo": "Найдено несколько пользователей с одинаковыми уникально идентифицирующими данными"
    },
    {
        "source": "I/O error on POST request for \"https://www.gosuslugi.ru/api/smev-converter/services/get\": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested excep",
        "target": "I/O error on POST request for \"https://www.gosuslugi.ru/api/smev-converter/services/get\": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested excep",
        "pseudo": "I/O error on POST request for \"https://www.gosuslugi.ru/api/smev-converter/services/get\""
    },
    {
        "source": "Error response from external service. Response code: 504 Gateway Timeout. Body: [<html>\r\n<head><title>504 Gateway Time-out</title></head>\r\n<body>\r\n<center><h1>504 Gateway Time-out</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n], url: [",
        "target": "Error response from external service. Response code: 504 Gateway Timeout. Body: [<html>\r\n<head><title>504 Gateway Time-out</title></head>\r\n<body>\r\n<center><h1>504 Gateway Time-out</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n], url: [",
        "pseudo": "Error response from external service. Response code: 504 Gateway Timeout. Body"
    },
    {
        "source": "ServiceDescriptor store client: Error on /v1/scenario/{serviceId} by serviceId: 10000000308; Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"Bad Request\",\"message\":\"BAD_REQUEST\",\"hint\":null,\"description\":\"Unexp",
        "target": "ServiceDescriptor store client: Error on /v1/scenario/{serviceId} by serviceId: [[target]]; Error response from external service. Response code: 400 Bad Request.",
        "pseudo": "ServiceDescriptor store client: Error on /v1/scenario/{serviceId} by serviceId"
    },
    {
        "source": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"Bad Request\",\"message\":\"BAD_REQUEST\",\"description\":\"Error response from external service. Response code: 500 Internal Server Error. Body: [{\\\"error\\\":{\\\"code\\\":3,",
        "target": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"Bad Request\",\"message\":\"BAD_REQUEST\",\"description\":\"Error response from external service. Response code: 500 Internal Server Error. Body: [{\\\"error\\\":{\\\"code\\\":3,",
        "pseudo": "500 Internal Server Error. Body: error code: 3"
    },
    {
        "source": "Error response from external service. Response code: 502 Bad Gateway. Body: [<!DOCTYPE html><html lang=\"en\"><head> <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> <meta charset=\"utf-8\"> <title>Портал государственных услуг Российской Федерации</",
        "target": "Error response from external service. Response code: 502 Bad Gateway. Body: [<!DOCTYPE html><html lang=\"en\"><head> <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> <meta charset=\"utf-8\"> <title>Портал государственных услуг Российской Федерации</",
        "pseudo": "Response code: 502 Bad Gateway. HTML: Портал государственных услуг Российской Федерации"
    },
    {
        "source": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"BAD_REQUEST\",\"message\":\"Bad Request\",\"description\":\"Unexpected server error: SessionCallback; CQL [INSERT INTO drafts (body,lock_date,lock_org_id,lock_user_id,ord",
        "target": "Error response from external service. Response code: 400 Bad Request. Body: [{\"status\":\"BAD_REQUEST\",\"message\":\"Bad Request\",\"description\":\"Unexpected server error: SessionCallback; CQL [INSERT INTO drafts (body,lock_date,lock_org_id,lock_user_id,ord",
        "pseudo": "Unexpected server error: SessionCallback; CQL [INSERT INTO drafts..."
    },
    {
        "source": "I/O error on POST request for \"http://p00pgunlbservices/api/nsi/v1/dictionary/EXTERNAL_BIC\": Connection reset; nested exception is java.net.SocketException: Connection reset",
        "target": "I/O error on POST request for \"http://p00pgunlbservices/api/nsi/v1/dictionary/EXTERNAL_BIC\": Connection reset; nested exception is java.net.SocketException: Connection reset",
        "pseudo": "I/O error on POST request for \"http://p00pgunlbservices/api/nsi/v1/dictionary/EXTERNAL_BIC\": Connection reset",
    },
    {
        "source": "Error response from external service. Response code: 401 Unauthorized. Body: [{\"code\":\"ESIA-005013\",\"message\":\"SecurityErrorEnum.expiredToken\"}], url: [http://esia.gosuslugi.ru/esia-rs/api/internal/v1/pso/srch/by-snils?snils=*** method: [GET]",
        "target": "Error response from external service. Response code: 401 Unauthorized. Body: [{\"code\":[[target]],\"message\":\"SecurityErrorEnum.expiredToken\"}], url: [http://esia.gosuslugi.ru/esia-rs/api/internal/v1/pso/srch/by-snils?snils=*** method: [GET]",
        "pseudo": "Response code: 401 Unauthorized. SecurityErrorEnum.expiredToken",
    },
    {
        "source": "Error response from external service. Response code: 503 Service Unavailable. Body: [<html>\r\n<head><title>503 Service Temporarily Unavailable</title></head>\r\n<body>\r\n<center><h1>503 Service Temporarily Unavailable</h1></center>\r\n<hr><center>nginx/1.1",
        "target": "Error response from external service. Response code: 503 Service Unavailable. Body: [<html>\r\n<head><title>503 Service Temporarily Unavailable</title></head>\r\n<body>\r\n<center><h1>503 Service Temporarily Unavailable</h1></center>\r\n<hr><center>nginx/1.1",
        "pseudo": "503 Service Temporarily Unavailable",
    },
    {
        "source": "Request processing failed; nested exception is ru.gosuslugi.pgu.common.core.exception.ExternalServiceException: Error response from external service. Response code: 504 Gateway Timeout. Body: [<html>\r\n<head><title>504 Gateway Time-out</title></head>\r",
        "target": "Request processing failed; nested exception is ru.gosuslugi.pgu.common.core.exception.ExternalServiceException: Error response from external service. Response code: 504 Gateway Timeout. Body: [<html>\r\n<head><title>504 Gateway Time-out</title></head>",
        "pseudo": "Response code: 504 Gateway Timeout",
    },
]
