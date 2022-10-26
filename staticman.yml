# Name of the property. You can have multiple properties with completely
# different config blocks for different sections of your site.
# For example, you can have one property to handle comment submission and
# another one to handle posts.
# To encrypt strings use the following endpoint:
# https://{your Staticman API URL}/v[2|3]/encrypt/{TEXT TO BE ENCRYPTED}

comments:
  # (*) REQUIRED
  #
  # Names of the fields the form is allowed to submit. If a field that is
  # not here is part of the request, an error will be thrown.
  allowedFields: ["name", "email", "url", "message"]

  # (*) REQUIRED WHEN USING NOTIFICATIONS
  #
  # When allowedOrigins is defined, only requests sent from one of the domains
  # listed will be accepted. The origin is sent as part as the `options` object
  # (e.g. <input name="options[origin]" value="http://yourdomain.com/post1")
  # allowedOrigins: ["yourdomain.com"]

  # (*) REQUIRED
  #
  # Name of the branch being used. Must match the one sent in the URL of the
  # request.
  branch: "master"

  commitMessage: "New comment by {fields.name}"

  # (*) REQUIRED
  #
  # Destination path (filename) for the data files. Accepts placeholders.
  filename: "comment-{@timestamp}"

  # The format of the generated data files. Accepted values are "json", "yaml"
  # or "frontmatter"
  format: "yaml"

  # List of fields to be populated automatically by Staticman and included in
  # the data file. Keys are the name of the field. The value can be an object
  # with a `type` property, which configures the generated field, or any value
  # to be used directly (e.g. a string, number or array)
  generatedFields:
    date:
      type: "date"
      options:
        format: "iso8601" # "iso8601" (default), "timestamp-seconds", "timestamp-milliseconds"

  # Whether entries need to be approved before they are published to the main
  # branch. If set to `true`, a pull request will be created for your approval.
  # Otherwise, entries will be published to the main branch automatically.
  moderation: true

  # Akismet spam detection.
  # akismet:
  #   enabled: true
  #   author: "name"
  #   authorEmail: "email"
  #   authorUrl: "url"
  #   content: "message"
  #   type: "comment"

  # Name of the site. Used in notification emails.
  # name: "Your Site"

  # Notification settings. When enabled, users can choose to receive notifications
  # via email when someone adds a reply or a new comment. This requires an account
  # with Mailgun, which you can get for free at http://mailgun.com.
  # notifications:
    # Enable notifications
    # enabled: true

    # (!) ENCRYPTED
    #
    # Mailgun API key
    # apiKey: ""

    # (!) ENCRYPTED
    #
    # Mailgun domain (encrypted)
    # domain: ""

  # (*) REQUIRED
  #
  # Destination path (directory) for the data files. Accepts placeholders.
  path: "docs/_data/comments/{options.slug}" # "_data/comments/{options.slug}" (default)

  # Names of required files. If any of these isn't in the request or is empty,
  # an error will be thrown.
  requiredFields: ["name", "email", "message"]

  # List of transformations to apply to any of the fields supplied. Keys are
  # the name of the field and values are possible transformation types.
  transforms:
    email: md5

  # reCaptcha
  # Register your domain at https://www.google.com/recaptcha/ and choose reCAPTCHA V2
  reCaptcha:
    enabled: true
    siteKey: "6LdRBykTAAAAAFB46MnIu6ixuxwu9W1ihFF8G60Q"
    # Encrypt reCaptcha secret key using Staticman /encrypt endpoint
    # For more information, https://staticman.net/docs/encryption
    secret: "PznnZGu3P6eTHRPLORniSq+J61YEf+A9zmColXDM5icqF49gbunH51B8+h+i2IvewpuxtA9TFoK68TuhUp/X3YKmmqhXasegHYabY50fqF9nJh9npWNhvITdkQHeaOqnFXUIwxfiEeUt49Yoa2waRR7a5LdRAP3SVM8hz0KIBT4="
