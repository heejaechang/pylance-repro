from issue8295_editable import Box, Domain, convert, identity, metadata_get


# SEMANTIC-TOKEN CHECK: imported symbols must retain semantic coloring.
# CONTROL: this file intentionally has no PEP 723 metadata.
converted_number = convert(1)
converted_text = convert("text")
boxed_text = Box("boxed")
identity_result = identity(boxed_text.value)
reduced_domain = Domain.REDUCED
signature_metadata = metadata_get("signature")

print(
    converted_number,
    converted_text,
    identity_result,
    reduced_domain,
    signature_metadata,
)
