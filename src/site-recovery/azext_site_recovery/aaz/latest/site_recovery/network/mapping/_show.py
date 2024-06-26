# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "site-recovery network mapping show",
)
class Show(AAZCommand):
    """Get the details of an ASR network mapping.

    :example: network mapping show
        az site-recovery network mapping show -g rg --fabric-name fabric_source_name -n network_mapping_src_to_recovery_name --network-name azureNetwork --vault-name vault_name
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.recoveryservices/vaults/{}/replicationfabrics/{}/replicationnetworks/{}/replicationnetworkmappings/{}", "2022-08-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.fabric_name = AAZStrArg(
            options=["--fabric-name"],
            help="Primary fabric name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.network_mapping_name = AAZStrArg(
            options=["-n", "--name", "--network-mapping-name"],
            help="Network mapping name.",
            required=True,
            id_part="child_name_3",
        )
        _args_schema.network_name = AAZStrArg(
            options=["--network-name"],
            help="Primary network name.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the recovery services vault.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ReplicationNetworkMappingsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReplicationNetworkMappingsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationNetworks/{networkName}/replicationNetworkMappings/{networkMappingName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "fabricName", self.ctx.args.fabric_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkMappingName", self.ctx.args.network_mapping_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkName", self.ctx.args.network_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.vault_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.fabric_specific_settings = AAZObjectType(
                serialized_name="fabricSpecificSettings",
            )
            properties.primary_fabric_friendly_name = AAZStrType(
                serialized_name="primaryFabricFriendlyName",
            )
            properties.primary_network_friendly_name = AAZStrType(
                serialized_name="primaryNetworkFriendlyName",
            )
            properties.primary_network_id = AAZStrType(
                serialized_name="primaryNetworkId",
            )
            properties.recovery_fabric_arm_id = AAZStrType(
                serialized_name="recoveryFabricArmId",
            )
            properties.recovery_fabric_friendly_name = AAZStrType(
                serialized_name="recoveryFabricFriendlyName",
            )
            properties.recovery_network_friendly_name = AAZStrType(
                serialized_name="recoveryNetworkFriendlyName",
            )
            properties.recovery_network_id = AAZStrType(
                serialized_name="recoveryNetworkId",
            )
            properties.state = AAZStrType()

            fabric_specific_settings = cls._schema_on_200.properties.fabric_specific_settings
            fabric_specific_settings.instance_type = AAZStrType(
                serialized_name="instanceType",
                flags={"required": True},
            )

            disc_azure_to_azure = cls._schema_on_200.properties.fabric_specific_settings.discriminate_by("instance_type", "AzureToAzure")
            disc_azure_to_azure.primary_fabric_location = AAZStrType(
                serialized_name="primaryFabricLocation",
            )
            disc_azure_to_azure.recovery_fabric_location = AAZStrType(
                serialized_name="recoveryFabricLocation",
            )

            disc_vmm_to_azure = cls._schema_on_200.properties.fabric_specific_settings.discriminate_by("instance_type", "VmmToAzure")
            disc_vmm_to_azure.location = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
