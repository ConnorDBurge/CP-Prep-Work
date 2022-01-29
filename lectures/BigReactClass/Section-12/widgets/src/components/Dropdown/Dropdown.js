import React from 'react';

const Dropdown = ({ options, selected, onSelectedChange }) => {

    const renderedOptions = options.map((option, index) => {

        if (option.value === JSON.parse(selected).value) {
            return null
        } else {
            return (
                <div
                    key={index}
                    className='item'
                    onClick={() => onSelectedChange(JSON.stringify(option))}>
                    {option.label}
                </div>
            );
        }
    });

    return (
        <div className='ui form'>
            <div className='field'>
                <label className='label'>Select a Color</label>
                <div className='ui selection dropdown visible active'>
                    <i className='dropdown icon'></i>
                    <div className='text'>{JSON.parse(selected).label}</div>
                    <div className="menu visible transition">
                        {renderedOptions}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dropdown;