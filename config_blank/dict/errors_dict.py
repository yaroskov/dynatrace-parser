errors = [
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
        "pseudo": "Должно возвращаться всегда единственное подразделение по окато ******, а не нашли ничего."
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
]
