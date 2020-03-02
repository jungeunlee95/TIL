```html
<b-table
  show-empty
  small
  stacked
  :items="instance.networkInterfaces"
  :fields="fields"
>
  <template v-slot:cell(privateIpAddresses)="row">
    <b-button v-b-toggle="row.item.networkInterfaceId">show privateIpAddresses</b-button>
    <!-- Elements to collapse -->
    <b-collapse :id="row.item.networkInterfaceId" class="mt-2">
      <b-card>
        <b-card-body v-for="privateIp in row.item.privateIpAddresses" v-bind:key="privateIp.id">
          privateIpAddress: {{privateIp.privateIpAddress}}<br>
          ipOwnerId: {{privateIp.ipOwnerId}}<br>
          publicDnsName: {{privateIp.publicDnsName}}<br>
          publicIp: {{privateIp.publicIp}}<br>
          privateDnsName: {{privateIp.privateDnsName}}<br>
        </b-card-body>
      </b-card>
    </b-collapse>
  </template>
</b-table>
```