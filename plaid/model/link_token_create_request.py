"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.413.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.country_code import CountryCode
    from plaid.model.link_token_account_filters import LinkTokenAccountFilters
    from plaid.model.link_token_create_hosted_link import LinkTokenCreateHostedLink
    from plaid.model.link_token_create_institution_data import LinkTokenCreateInstitutionData
    from plaid.model.link_token_create_request_auth import LinkTokenCreateRequestAuth
    from plaid.model.link_token_create_request_base_report import LinkTokenCreateRequestBaseReport
    from plaid.model.link_token_create_request_deposit_switch import LinkTokenCreateRequestDepositSwitch
    from plaid.model.link_token_create_request_employment import LinkTokenCreateRequestEmployment
    from plaid.model.link_token_create_request_identity_verification import LinkTokenCreateRequestIdentityVerification
    from plaid.model.link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
    from plaid.model.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
    from plaid.model.link_token_create_request_statements import LinkTokenCreateRequestStatements
    from plaid.model.link_token_create_request_transfer import LinkTokenCreateRequestTransfer
    from plaid.model.link_token_create_request_update import LinkTokenCreateRequestUpdate
    from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
    from plaid.model.link_token_eu_config import LinkTokenEUConfig
    from plaid.model.link_token_investments import LinkTokenInvestments
    from plaid.model.link_token_investments_auth import LinkTokenInvestmentsAuth
    from plaid.model.products import Products
    globals()['CountryCode'] = CountryCode
    globals()['LinkTokenAccountFilters'] = LinkTokenAccountFilters
    globals()['LinkTokenCreateHostedLink'] = LinkTokenCreateHostedLink
    globals()['LinkTokenCreateInstitutionData'] = LinkTokenCreateInstitutionData
    globals()['LinkTokenCreateRequestAuth'] = LinkTokenCreateRequestAuth
    globals()['LinkTokenCreateRequestBaseReport'] = LinkTokenCreateRequestBaseReport
    globals()['LinkTokenCreateRequestDepositSwitch'] = LinkTokenCreateRequestDepositSwitch
    globals()['LinkTokenCreateRequestEmployment'] = LinkTokenCreateRequestEmployment
    globals()['LinkTokenCreateRequestIdentityVerification'] = LinkTokenCreateRequestIdentityVerification
    globals()['LinkTokenCreateRequestIncomeVerification'] = LinkTokenCreateRequestIncomeVerification
    globals()['LinkTokenCreateRequestPaymentInitiation'] = LinkTokenCreateRequestPaymentInitiation
    globals()['LinkTokenCreateRequestStatements'] = LinkTokenCreateRequestStatements
    globals()['LinkTokenCreateRequestTransfer'] = LinkTokenCreateRequestTransfer
    globals()['LinkTokenCreateRequestUpdate'] = LinkTokenCreateRequestUpdate
    globals()['LinkTokenCreateRequestUser'] = LinkTokenCreateRequestUser
    globals()['LinkTokenEUConfig'] = LinkTokenEUConfig
    globals()['LinkTokenInvestments'] = LinkTokenInvestments
    globals()['LinkTokenInvestmentsAuth'] = LinkTokenInvestmentsAuth
    globals()['Products'] = Products


class LinkTokenCreateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('country_codes',): {
            'min_items': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'client_name': (str,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'country_codes': ([CountryCode],),  # noqa: E501
            'user': (LinkTokenCreateRequestUser,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'products': ([Products],),  # noqa: E501
            'additional_consented_products': ([Products],),  # noqa: E501
            'required_if_supported_products': ([Products],),  # noqa: E501
            'webhook': (str,),  # noqa: E501
            'access_token': (str,),  # noqa: E501
            'link_customization_name': (str,),  # noqa: E501
            'redirect_uri': (str,),  # noqa: E501
            'android_package_name': (str,),  # noqa: E501
            'institution_data': (LinkTokenCreateInstitutionData,),  # noqa: E501
            'account_filters': (LinkTokenAccountFilters,),  # noqa: E501
            'eu_config': (LinkTokenEUConfig,),  # noqa: E501
            'institution_id': (str,),  # noqa: E501
            'payment_initiation': (LinkTokenCreateRequestPaymentInitiation,),  # noqa: E501
            'deposit_switch': (LinkTokenCreateRequestDepositSwitch,),  # noqa: E501
            'employment': (LinkTokenCreateRequestEmployment,),  # noqa: E501
            'income_verification': (LinkTokenCreateRequestIncomeVerification,),  # noqa: E501
            'base_report': (LinkTokenCreateRequestBaseReport,),  # noqa: E501
            'auth': (LinkTokenCreateRequestAuth,),  # noqa: E501
            'transfer': (LinkTokenCreateRequestTransfer,),  # noqa: E501
            'update': (LinkTokenCreateRequestUpdate,),  # noqa: E501
            'identity_verification': (LinkTokenCreateRequestIdentityVerification,),  # noqa: E501
            'statements': (LinkTokenCreateRequestStatements,),  # noqa: E501
            'user_token': (str,),  # noqa: E501
            'investments': (LinkTokenInvestments,),  # noqa: E501
            'investments_auth': (LinkTokenInvestmentsAuth,),  # noqa: E501
            'hosted_link': (LinkTokenCreateHostedLink,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'client_name': 'client_name',  # noqa: E501
        'language': 'language',  # noqa: E501
        'country_codes': 'country_codes',  # noqa: E501
        'user': 'user',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'products': 'products',  # noqa: E501
        'additional_consented_products': 'additional_consented_products',  # noqa: E501
        'required_if_supported_products': 'required_if_supported_products',  # noqa: E501
        'webhook': 'webhook',  # noqa: E501
        'access_token': 'access_token',  # noqa: E501
        'link_customization_name': 'link_customization_name',  # noqa: E501
        'redirect_uri': 'redirect_uri',  # noqa: E501
        'android_package_name': 'android_package_name',  # noqa: E501
        'institution_data': 'institution_data',  # noqa: E501
        'account_filters': 'account_filters',  # noqa: E501
        'eu_config': 'eu_config',  # noqa: E501
        'institution_id': 'institution_id',  # noqa: E501
        'payment_initiation': 'payment_initiation',  # noqa: E501
        'deposit_switch': 'deposit_switch',  # noqa: E501
        'employment': 'employment',  # noqa: E501
        'income_verification': 'income_verification',  # noqa: E501
        'base_report': 'base_report',  # noqa: E501
        'auth': 'auth',  # noqa: E501
        'transfer': 'transfer',  # noqa: E501
        'update': 'update',  # noqa: E501
        'identity_verification': 'identity_verification',  # noqa: E501
        'statements': 'statements',  # noqa: E501
        'user_token': 'user_token',  # noqa: E501
        'investments': 'investments',  # noqa: E501
        'investments_auth': 'investments_auth',  # noqa: E501
        'hosted_link': 'hosted_link',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, client_name, language, country_codes, user, *args, **kwargs):  # noqa: E501
        """LinkTokenCreateRequest - a model defined in OpenAPI

        Args:
            client_name (str): The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display \"This Application\" instead.
            language (str): The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).  Supported languages are: - Danish (`'da'`) - Dutch (`'nl'`) - English (`'en'`) - Estonian (`'et'`) - French (`'fr'`) - German (`'de'`) - Italian (`'it'`) - Latvian (`'lv'`) - Lithuanian (`'lt'`) - Norwegian (`'no'`) - Polish (`'pl'`) - Portuguese (`'pt'`) - Romanian (`'ro'`) - Spanish (`'es'`) - Swedish (`'sv'`)  When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.
            country_codes ([CountryCode]): Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.  If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.  If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.  If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.
            user (LinkTokenCreateRequestUser):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            products ([Products]): List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.  `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.  The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a \"Connectivity not supported\" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be included via the [`required_if_supported_products`](https://plaid.com/docs/api/tokens/#link-token-create-request-required-if-supported-products) field, or can be initialized by calling the endpoint after obtaining an access token. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).  Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.  In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.. [optional]  # noqa: E501
            additional_consented_products ([Products]): (Beta) This field has no effect unless you are participating in the [Data Transparency](https://plaid.com/docs/link/data-transparency-messaging-migration-guide) beta program. List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.  `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.  Institutions that do not support these products will still be shown in Link. [optional]  # noqa: E501
            required_if_supported_products ([Products]): List of Plaid product(s) you wish to use only if the institution and account(s) selected by the user support the product. Institutions that do not support these products will still be shown in Link. The products will only be extracted and billed if the user selects an institution and account type that supports them.  There should be no overlap between `products` and `required_if_supported_products`. The `products` array must have at least one product.  For more details on using this feature, see [Required if Supported Products](https://www.plaid.com/docs/link/initializing-products/#required-if-supported-products).. [optional]  # noqa: E501
            webhook (str): The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead.. [optional]  # noqa: E501
            access_token (str): The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow.. [optional]  # noqa: E501
            link_customization_name (str): The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.. [optional]  # noqa: E501
            redirect_uri (str): A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank.. [optional]  # noqa: E501
            android_package_name (str): The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead.. [optional]  # noqa: E501
            institution_data (LinkTokenCreateInstitutionData): [optional]  # noqa: E501
            account_filters (LinkTokenAccountFilters): [optional]  # noqa: E501
            eu_config (LinkTokenEUConfig): [optional]  # noqa: E501
            institution_id (str): Used for certain Europe-only configurations, as well as certain legacy use cases in other regions.. [optional]  # noqa: E501
            payment_initiation (LinkTokenCreateRequestPaymentInitiation): [optional]  # noqa: E501
            deposit_switch (LinkTokenCreateRequestDepositSwitch): [optional]  # noqa: E501
            employment (LinkTokenCreateRequestEmployment): [optional]  # noqa: E501
            income_verification (LinkTokenCreateRequestIncomeVerification): [optional]  # noqa: E501
            base_report (LinkTokenCreateRequestBaseReport): [optional]  # noqa: E501
            auth (LinkTokenCreateRequestAuth): [optional]  # noqa: E501
            transfer (LinkTokenCreateRequestTransfer): [optional]  # noqa: E501
            update (LinkTokenCreateRequestUpdate): [optional]  # noqa: E501
            identity_verification (LinkTokenCreateRequestIdentityVerification): [optional]  # noqa: E501
            statements (LinkTokenCreateRequestStatements): [optional]  # noqa: E501
            user_token (str): A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user.. [optional]  # noqa: E501
            investments (LinkTokenInvestments): [optional]  # noqa: E501
            investments_auth (LinkTokenInvestmentsAuth): [optional]  # noqa: E501
            hosted_link (LinkTokenCreateHostedLink): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.client_name = client_name
        self.language = language
        self.country_codes = country_codes
        self.user = user
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, client_name, language, country_codes, user, *args, **kwargs):  # noqa: E501
        """LinkTokenCreateRequest - a model defined in OpenAPI

        Args:
            client_name (str): The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value longer than 30 characters is provided, Link will display \"This Application\" instead.
            language (str): The language that Link should be displayed in. When initializing with Identity Verification, this field is not used; for more details, see [Identity Verification supported languages](https://www.plaid.com/docs/identity-verification/#supported-languages).  Supported languages are: - Danish (`'da'`) - Dutch (`'nl'`) - English (`'en'`) - Estonian (`'et'`) - French (`'fr'`) - German (`'de'`) - Italian (`'it'`) - Latvian (`'lv'`) - Lithuanian (`'lt'`) - Norwegian (`'no'`) - Polish (`'pl'`) - Portuguese (`'pt'`) - Romanian (`'ro'`) - Spanish (`'es'`) - Swedish (`'sv'`)  When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.
            country_codes ([CountryCode]): Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see https://plaid.com/global/.  If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. Access to European institutions requires additional compliance steps. To request access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.  If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`, or the customization may not be applied.  If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.
            user (LinkTokenCreateRequestUser):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            products ([Products]): List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted (unless you are using update mode to add Income or Assets to an Item); required otherwise.  `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically be initialized when any other product is initialized.  The products specified here will determine which institutions will be available to your users in Link. Only institutions that support *all* requested products can be selected; a if a user attempts to select an institution that does not support a listed product, a \"Connectivity not supported\" error message will appear in Link. To maximize the number of institutions available, initialize Link with the minimal product set required for your use case. Additional products can be included via the [`required_if_supported_products`](https://plaid.com/docs/api/tokens/#link-token-create-request-required-if-supported-products) field, or can be initialized by calling the endpoint after obtaining an access token. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/initializing-products/).  Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.  In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.. [optional]  # noqa: E501
            additional_consented_products ([Products]): (Beta) This field has no effect unless you are participating in the [Data Transparency](https://plaid.com/docs/link/data-transparency-messaging-migration-guide) beta program. List of additional Plaid product(s) you wish to collect consent for. These products will not be billed until you start using them by calling the relevant endpoints.  `balance` is *not* a valid value, the Balance product does not require explicit initialization and will automatically have consent collected.  Institutions that do not support these products will still be shown in Link. [optional]  # noqa: E501
            required_if_supported_products ([Products]): List of Plaid product(s) you wish to use only if the institution and account(s) selected by the user support the product. Institutions that do not support these products will still be shown in Link. The products will only be extracted and billed if the user selects an institution and account type that supports them.  There should be no overlap between `products` and `required_if_supported_products`. The `products` array must have at least one product.  For more details on using this feature, see [Required if Supported Products](https://www.plaid.com/docs/link/initializing-products/#required-if-supported-products).. [optional]  # noqa: E501
            webhook (str): The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks) and Identity Verification are configured via the Dashboard instead.. [optional]  # noqa: E501
            access_token (str): The `access_token` associated with the Item to update or reference, used when updating, modifying, or accessing an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow.. [optional]  # noqa: E501
            link_customization_name (str): The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.. [optional]  # noqa: E501
            redirect_uri (str): A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). If initializing on Android, `android_package_name` must be specified instead and `redirect_uri` should be left blank.. [optional]  # noqa: E501
            android_package_name (str): The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). When creating a `link_token` for initializing Link on other platforms, `android_package_name` must be left blank and `redirect_uri` should be used instead.. [optional]  # noqa: E501
            institution_data (LinkTokenCreateInstitutionData): [optional]  # noqa: E501
            account_filters (LinkTokenAccountFilters): [optional]  # noqa: E501
            eu_config (LinkTokenEUConfig): [optional]  # noqa: E501
            institution_id (str): Used for certain Europe-only configurations, as well as certain legacy use cases in other regions.. [optional]  # noqa: E501
            payment_initiation (LinkTokenCreateRequestPaymentInitiation): [optional]  # noqa: E501
            deposit_switch (LinkTokenCreateRequestDepositSwitch): [optional]  # noqa: E501
            employment (LinkTokenCreateRequestEmployment): [optional]  # noqa: E501
            income_verification (LinkTokenCreateRequestIncomeVerification): [optional]  # noqa: E501
            base_report (LinkTokenCreateRequestBaseReport): [optional]  # noqa: E501
            auth (LinkTokenCreateRequestAuth): [optional]  # noqa: E501
            transfer (LinkTokenCreateRequestTransfer): [optional]  # noqa: E501
            update (LinkTokenCreateRequestUpdate): [optional]  # noqa: E501
            identity_verification (LinkTokenCreateRequestIdentityVerification): [optional]  # noqa: E501
            statements (LinkTokenCreateRequestStatements): [optional]  # noqa: E501
            user_token (str): A user token generated using `/user/create`. Any Item created during the Link session will be associated with the user.. [optional]  # noqa: E501
            investments (LinkTokenInvestments): [optional]  # noqa: E501
            investments_auth (LinkTokenInvestmentsAuth): [optional]  # noqa: E501
            hosted_link (LinkTokenCreateHostedLink): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.client_name = client_name
        self.language = language
        self.country_codes = country_codes
        self.user = user
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
