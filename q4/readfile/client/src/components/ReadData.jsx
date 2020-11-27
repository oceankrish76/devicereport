import React, { useState, useEffect } from 'react'
// semantic-ui table
import { Table } from 'semantic-ui-react'

const ReadData = () => {
	// Declare a new state variable data
	const [ data, setData ] = useState([])

	const getData = async () => {
		const res = await fetch('/data', {
			headers: {
				'Content-Type': 'application/json',
				Accept: 'application/json'
			}
		})
		//const response = res.json()

		const datavalue = await res.json()
		console.table(datavalue)

		// data state
		setData(datavalue)
	}
	useEffect(() => {
		getData()
	}, [])

	return (
		<React.Fragment>
			<div className="center-container">
				<h2>Data from file</h2>
				<Table celled>
					<Table.Header>
						<Table.Row>
							<Table.HeaderCell>ID</Table.HeaderCell>
							<Table.HeaderCell>IMEI</Table.HeaderCell>
							<Table.HeaderCell>Name</Table.HeaderCell>
						</Table.Row>
					</Table.Header>

					<Table.Body>
						{data.map((el) => {
							return (
								<Table.Row key={el.ID}>
									<Table.Cell>{el.ID}</Table.Cell>
									<Table.Cell>{el.IMEI}</Table.Cell>
									<Table.Cell>{el.Name}</Table.Cell>
								</Table.Row>
							)
						})}
					</Table.Body>
				</Table>
			</div>
		</React.Fragment>
	)
}

export default ReadData
