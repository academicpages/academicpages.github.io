from _typeshed import Incomplete

from stripe.stripe_object import StripeObject as StripeObject

class ErrorObject(StripeObject):
    def refresh_from(
        self,
        values,
        api_key: Incomplete | None = ...,
        partial: bool = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        last_response: Incomplete | None = ...,
    ): ...

class OAuthErrorObject(StripeObject):
    def refresh_from(
        self,
        values,
        api_key: Incomplete | None = ...,
        partial: bool = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        last_response: Incomplete | None = ...,
    ): ...
